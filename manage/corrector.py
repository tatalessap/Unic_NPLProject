from manage.toManageData import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
import operator

"""
check if there are wrong words in the sentence. 
pathFile is the path where the dictionary is located. 
sentence, on the other hand, is the list of messages to check.
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
creates a list of correct words within the sentence
"""
def getGoodWord(pathFile, sentence):
    goodWords = []

    sentenceList = splitSentence(sentence) #split sentence, no special character

    with open(pathFile) as f:
        setDictionary = json.load(f)  # dic

    for word in sentenceList:
        if str(len(word)) in setDictionary.keys():
            if word in setDictionary.get(str(len(word))) and word != ' ':
                goodWords.append(word)

    return goodWords


"""
getAlternative is the function to use depending on the model, 
badWord is the word, 
goodWords serves in case you are using word2vect, nameModel is a flag to know how to use getAlternative
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


"""
returns the list of possible words sorted in descending order according to the score
"""
def spellChecker(word, possibleWords):
    result = {}
    for el in possibleWords:
        score = getPossibleElement(word, el[0], el[1])
        result[el[0]] = score

    result = sorted(result.items(), reverse=True, key=lambda x: x[1])

    return result[:7]

"""
returns the score
"""
def getPossibleElement(word, possibleWord, similarity, constant=0.5):
    score = 0
    if len(possibleWord) > 2:
        if similarity > constant:
            score = score + 2
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
