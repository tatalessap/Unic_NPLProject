from manage.toManageData import *
from manage.toCreateSetWords import *
from manage.wordEmbeddings import *
import Levenshtein

"""
"""


def checkSentence(path, nameFile, sentence, model):
    sentenceList = splitSentence(sentence)

    listPrevious = []
    possibleWordsList = []

    with open(path + nameFile) as f:
        dataFile = json.load(f)

    for word in sentenceList:
        if str(len(word)) in dataFile.keys():
            if word not in dataFile.get(str(len(word))):
                print('\nbad:' + word)
                possibleWords = model.predict(listPrevious, topn=10)
                (list(map(lambda x: possibleWordsList.append(x[0]), possibleWords)))
                print(getdistanceLevenshtein(word, possibleWordsList))
            else:
                listPrevious.append(word)
"""
"""
def splitSentence(sentence):
    remove = string.punctuation
    pattern = r"[{}]".format(remove)  # create the pattern

    sentence = re.sub(pattern, "", sentence)
    sentenceList = re.split(' ', sentence)
    sentenceList = list(map(lambda x: x.lower(), sentenceList))

    return sentenceList
