# simple ngram utility library by Maurizio Atzori. All right reserved 2016-2017


def ngram(w,n=2):
	"Rome => [Ro, om, me] with n=2, or [Rom,ome] with n=3"
	return [ w[i:i+n] for i in range(len(w)-n+1) ]

def xngram(w,n=2):
	""" as ngram but with generators. 50% slower than ngram but saves memory """
	for i in range(len(w)-n+1):
		yield w[i:i+n]



# pairize similarity
from gensim import corpora, models, similarities

def index(txtfile):
	"get a text file with a word per line; return a gensim index"
	words = [w for w in open(txtfile)]
	#words = [w for w in open(txtfile)]	
	words = [w.strip().lower() for w in words]
	docs = [ngram(w) for w in words] # a corpus where each document is made of a pairized word
	dictionary = corpora.Dictionary(docs)
	corpus = [dictionary.doc2bow(doc) for doc in docs]
	index = similarities.MatrixSimilarity(corpus) # on RAM
	#index = similarities.Similarity('./index/'+txtfile, corpus, num_features=30*30)
	index.dictionary = dictionary
	index.words = words
	return index

def similar(index, query, n=1):
	index.num_best = n
	query_vec = index.dictionary.doc2bow( ngram(query.lower()) )
	solutions = index[query_vec] # 0 = the most similar
	return [(index.words[solution[0]],solution[1]) for solution in solutions]


# edit distance from Wikipedia
def levenshtein(s1, s2):
	if len(s1) < len(s2):
		return levenshtein(s2, s1)

	# len(s1) >= len(s2)
	if len(s2) == 0:
		return len(s1)

	previous_row = range(len(s2) + 1)
	for i, c1 in enumerate(s1):
		current_row = [i + 1]
		for j, c2 in enumerate(s2):
			insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
			deletions = current_row[j] + 1	   # than s2
			substitutions = previous_row[j] + (c1 != c2)
			current_row.append(min(insertions, deletions, substitutions))
		previous_row = current_row
	
	return previous_row[-1]

def similar2(index, query, n=30):
	sims = similar(index, query, n)
	x = sorted([(word,score,levenshtein(query,word)) for word,score in sims], key=lambda s: s[2] -s[1] )
	return x



def similar2_distance(index,word1,word2):
	print(len(index.dictionary))
	#return 10  
	a = [0.0]*len(index.dictionary)
	b = [0.0]*len(index.dictionary)

	bow1 = index.dictionary.doc2bow(ngram(word1))
	bow2 = index.dictionary.doc2bow(ngram(word2))
	for e,i in bow1: a[e] = i +0.0
	for e,i in bow2: b[e] = i +0.0
  
	from scipy.spatial.distance import cosine
	import numpy
	cos = cosine(a,b)
	#result = numpy.dot( numpy.array(A)[:,0], B)
	#cos = sum( [v1[i]*v2[i] for i in set(v1.keys()).intersection(set(v2.keys())) ] )

	mydist = 0.0
	for i in range(len(index.dictionary)):
		mydist += pow(a[i] - b[i],2.0)

	import math
	dist = {
		'levenshtein': levenshtein(word1,word2),
		'cos-dist': int(cos  *1000)/1000,
		'dist': math.sqrt(mydist)
		#'dot': math.sqrt( numpy.dot(a,[-1*x for x in b]))
	}
	return dist
