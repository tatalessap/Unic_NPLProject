from manage.toManageData import *
from manage.wordEmbeddings import *

"""
"""
def checkSentence2(pathFile, sentence, model, softness):
    sentenceList = splitSentence(sentence)

    goodWords = []
    badWords = []
    possibleWordsList = []
    listFinal = []


    with open(pathFile, encoding='utf-8') as f:
        dataFile = json.load(f)

    for word in sentenceList:
        if str(len(word)) in dataFile.keys():
            if word not in dataFile.get(str(len(word))):
                print('\nbad:' + word)
                badWords.append(word)
            else:
                goodWords.append(word)

    if not len(badWords) == 0:
        for word in badWords:

            possibleWords = model.predict(goodWords, topn=50)

            (list(map(lambda x: possibleWordsList.append(x[0]), possibleWords)))

            wordsWithFirstCharacter = list(filter(lambda x: x[0] == word[0], dataFile.get(str(len(word)))))

            listFirsCharacter = (getDistanceLevenshtein(word, wordsWithFirstCharacter, 0))

            listPossible = (getDistanceLevenshtein(word, possibleWordsList, softness))

            """
            if len(possibleWordsList) > 3:
                listFinal = possibleWordsList[:4]
            else:
                listFinal = union(listFinal, possibleWordsList)

            if len(listFirsCharacter) > 2:
                listFinal = union(listFinal, listFirsCharacter[:3])
            else:
                listFinal = union(listFinal, listFirsCharacter)

            print([x for x in range(len(listFinal))])
            print(listFinal)
            
            """

            print(listFirsCharacter)
            print(listPossible)

            print("insert new word:")

            new_word = input()

            sentenceList[sentenceList.index(word)] = new_word

    print(sentenceList)

    return sentenceList



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
