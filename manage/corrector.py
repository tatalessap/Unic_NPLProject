from manage.toManageData import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
import operator

"""
With a dictionary, this method check a sentence, and return a list of good words and a list of bad words, if there are 
some in a sentence.
"""
def checkSentence(pathFile, sentence):
    goodWords = []
    badWords = []

    sentenceList = splitSentence(sentence) #split sentence, no special character

    with open(pathFile) as f:
        setDictionary = json.load(f)  # dic

    for word in sentenceList:
        if str(len(word)) in setDictionary.keys():
            if word not in setDictionary.get(str(len(word))) and word!=' ':
                badWords.append(word)
            else:
                goodWords.append(word)

    return badWords, goodWords


"""
@:parameter getAlternative: the method of the model dedicate to give a list of possible words to substitute a bad word
For each bad word, print a list of possible substitute by method of the model
ft --> fast text
w2v --> word2vect
"""
def getPossibleWords(getAlternative, badWord, goodWords, nameModel):

    if nameModel == "ft":
        possibleWords = getAlternative(badWord)
    elif nameModel == "w2v":
        if goodWords == []:
            return []
        else:
            possibleWords = getAlternative(goodWords)
    else:
        return []

    return spellChecker(badWord, possibleWords)



def spellChecker(word, possibleWords):
    result = {}
    for el in possibleWords:
        score = getPossibleElement(word, el[0], el[1])
        result[el[0]] = score

    result = sorted(result.items(), reverse=True, key=lambda x: x[1])

    #print(result)

    return result[:7]


def getPossibleElement(word, possibleWord, similarity, constant=0.5):
    score = 0
    if len(possibleWord) > 2:
        if similarity > constant:
            if len(word) == len(possibleWord):
                score = score + 1
            if word[0] == possibleWord[0]:
                score = score + 2
            if word[len(word)-1] == possibleWord[len(possibleWord)-1]:
                score = score + 2
            if Levenshtein.distance(word, possibleWord) < 1:
                score = score + 5
            elif Levenshtein.distance(word, possibleWord) < 4:
                score = score + 3
    return score
