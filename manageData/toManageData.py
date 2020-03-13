import collections
import json


"""
by https://nlp.stanford.edu/IR-book/html/htmledition/edit-distance-1.html
Levenshtein distance
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


def createMatrixSimByDic(dic : dict):
    maxiMatrix = {}

    for key in dic.keys():
        maxiMatrix[key] = createMatrixSim(dic.get(key))

    #print(listKey)

    #maxiMatrix['2'] = createMatrixSim(dic.get('2'))


    return maxiMatrix


def createMatrixSim(listEl):
    matrixSim = {}

    for j in listEl:
        for i in listEl:
            matrixSim[i + ' ' + j] = distanceLevenshtein(i, j)

    return matrixSim


def createFileJson(list):
    data = {}

    for el in list:
        if el != '':
            if not (len(el) in data.keys()):
                data[len(el)] = [el]
            else:
                data.get(len(el)).append(el)
    sortedSavedJson(data, 'wordsByLen.json')


def sortedSavedJson(data, nameJson):
    od = collections.OrderedDict(sorted(data.items()))

    with open(nameJson, "w") as outfile:
        json.dump(od, outfile)
