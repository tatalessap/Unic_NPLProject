from manage.toManageData import *
from manage.wordEmbeddings import *

"""
"""
def checkSentence(pathFile, sentence, model):
    sentenceList = splitSentence(sentence)

    listPrevious = []
    possibleWordsList = []

    with open(pathFile) as f:
        dataFile = json.load(f)

    for word in sentenceList:
        if str(len(word)) in dataFile.keys():
            if word not in dataFile.get(str(len(word))):
                print('\nbad:' + word)
                possibleWords = model.predict(listPrevious, topn=30)
                (list(map(lambda x: possibleWordsList.append(x[0]), possibleWords)))
                print(getDistanceLevenshtein(word, possibleWordsList))
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
