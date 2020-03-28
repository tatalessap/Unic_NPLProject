import json

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def unionDataByData(data1, data2):
    dataFinal = {}

    for el in data1.keys():
        if not(el in data2.keys()):
            dataFinal[el] = data1.get(el)
        else:
            dataFinal[el] = union(data1.get(el), data2.get(el))

    return dataFinal


def unionDataByFileJson(pathfileJson1, pathfileJson2):

    with open(pathfileJson1) as f:
        data1 = json.load(f)

    with open(pathfileJson2) as f:
        data2 = json.load(f)

    dataFinal = unionDataByData(data1, data2)

    return dataFinal

def createDocWordsText(nameFileText):
    words = open(nameFileText, "r")
    wordsFun = words.readlines()
    list = []
    for line in wordsFun:
        line = line.rstrip("\n")
        list.append(line)
    words.close()

    return list

def extractListByDic(dic, min):
    listD = []
    for k in dic.keys():
        if dic[k] <= min:
            listD.append(k)

    return listD