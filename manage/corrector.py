from manage.toManageData import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
"""
"""
def checkSentence(pathFile, sentence):
    badWords = []
    sentenceList = splitSentence(sentence)

    goodWords = []
    badWords = []
    possibleWordsList = []
    listFinal = []

    with open(pathFile, encoding='utf-8') as f:
        setDictionary = json.load(f)  # dic

    for word in sentenceList:
        if str(len(word)) in setDictionary.keys():
            if word not in setDictionary.get(str(len(word))):
                badWords.append(word)
            else:
                goodWords.append(word)

    return badWords, goodWords


def getPossibleWordsByContext(model, badWords, goodWords):
    possibleWordsList = []

    for word in badWords:
        possibleWords = model.predict(goodWords)

        list(map(lambda x: possibleWordsList.append(x[0]), possibleWords))

        print(getDistanceLevenshtein(word, possibleWordsList))


def getPossibleWordBySimilar(model, badWords):
    possibleWordsList = []

    for word in badWords:
        print(predict(model, word))
