from manage.utilis import *
import collections
import json
import Levenshtein

"""
by https://nlp.stanford.edu/IR-book/html/htmledition/edit-distance-1.html
Levenshtein distance
@:parameter string1:
@:parameter string2:
two strings to calculate distance
"""
def distanceLevenshtein(string1, string2):
    if string1 == "":
        return len(string2)
    if string2 == "":
        return len(string1)
    if string1[-1] == string2[-1]:
        cost = 0
    else:
        cost = 1

    res = min([distanceLevenshtein(string1[:-1], string2) + 1,
               distanceLevenshtein(string1, string2[:-1]) + 1,
               distanceLevenshtein(string1[:-1], string2[:-1]) + cost])

    return res


"""
Create the similarity matrix by list and word
"""
def getdistanceLevenshtein(word, listEl):
    minDistance = 100
    minWords = []
    minDistances = []
    for el in listEl:
        d = Levenshtein.distance(str(word), str(el))
        if d < minDistance:
            minDistance = d
            minWord = el
        if d == minDistance:
            minWords.append(str(el))
            minDistances.append(d)

    print(minDistances)

    return minWords

"""
Create file json with len-key
"""
def createFileJsonByLen(list, nameJson):
    data = {}

    for el in list:
        if el != '':
            if not (len(el) in data.keys()):
                data[len(el)] = [el.lower()]
            else:
                data.get(len(el)).append(el.lower())

    sortedSavedJson(data, nameJson)

""
def sortedSavedJson(data, nameJson):
    od = collections.OrderedDict(sorted(data.items()))

    with open(nameJson, "w") as outfile:
        json.dump(od, outfile)

""
def createListBadWords(path, nameFileMessages, nameFile):
    key = "bad"
    badWords = {key: []}

    with open(path + nameFileMessages) as f:
        dataMessages = json.load(f)

    with open(path + nameFile) as f:
        dataFile = json.load(f)

    for k in dataMessages.keys():
        for eachWord in dataMessages.get(k):
            if not (eachWord in dataFile.get(k)):
                badWords.get(key).append(eachWord)

    sortedSavedJson(badWords, "onlyBadWords.json")



