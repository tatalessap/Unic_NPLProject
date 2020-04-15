import gensim
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models import Phrases, TfidfModel
from gensim.models.phrases import Phraser
from gensim.test.utils import datapath
from gensim.models.word2vec import Word2Vec, Text8Corpus
import json
import logging

class ModelWord2Vec:
    """path è la stringa che indica o il corpus su cui lavorare o il modello da caricare """

    def __init__(self, path, existModel=False):
        """se abbiamo il modello pronto existModel va segnato a true"""
        if existModel == False:
            self.model = self.createModel(path)
        else:
            self.model = Word2Vec.load(path)

    def createModel(self, pathCorpus, min_count=5, size=300, workers=8, window=5, iter=5, sg=1, negative=10):
        sentences = Text8Corpus(datapath(pathCorpus))
        model = Word2Vec(sentences,
                         min_count=min_count,  # Ignore words that appear less than this
                         size=size,  # Dimensionality of word embeddings
                         workers=workers,  # Number of processors
                         window=window,  # Context window for words during training
                         iter=iter,  # Number of epochs training over corpus
                         sg=sg,  # skip gram true
                         negative=negative)
        return model

    def predict(self, listOfWord, probability=0, topn=50):
        listOfWord = self.checkList(listOfWord)
        if listOfWord == []:
            return []
        else:
            predict = self.model.predict_output_word(listOfWord, topn=topn)
            return list(filter(lambda x: x[1] > probability, predict))




    def train(self, pathCorpus, epochs=60, compute_loss=True):
        sentences = Text8Corpus(datapath(pathCorpus))
        self.model.train(sentences, epochs=epochs, total_examples=self.model.corpus_count, compute_loss=compute_loss)

    def trainMoreSentence(self, moreSentence, epochs=60, compute_loss=True):
        self.model.build_vocab(moreSentence, update=True)
        self.model.train(moreSentence, epochs=epochs, total_examples=self.model.corpus_count, compute_loss=compute_loss)

    def checkList(self, listGoodW):
        newList = []
        for el in listGoodW:
            if el in list(self.model.wv.vocab.keys()):
                newList.append(el)

        return newList


"""funzioni utili"""
def cleanTextBadWord(text, key, badWord):
    """pulizia messaggi da file json passando il file json dei messaggi, la chiave su cui cercare
    e il file json della badWord"""
    from string import punctuation
    clean_text = {}
    bad_word = {}

    with open(text) as file:
        clean_text = json.load(file)

    with open(badWord) as file:
        bad_word = json.load(file)

    clean_text = clean_text(key)
    tmp = []
    for text in clean_text:
        tmp.append(" ".join(text.split()))
    clean_text = []
    clean_text = [''.join([c for c in text if c not in punctuation]) for text in tmp]
    bad_word = bad_word.get('bad')

    for b in bad_word:
        for m in clean_text:
            if b in m:
                clean_text.pop(clean_text.index(m))

    return clean_text


def createCorpusFromCleanText(clean_text, name='clean_text.txt'):
    with open(name, 'w') as f:
        for m in clean_text:
            f.writelines(m)


