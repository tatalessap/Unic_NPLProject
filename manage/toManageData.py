from manage.utilis import *
from manage.utilis import *
import collections
import json
import Levenshtein
from bs4 import BeautifulSoup
import re
import string
import json


"""
Create the similarity matrix by list and word
"""
def getDistanceLevenshtein(word, listEl):
    lenDis = {}
    minWords = []
    minDist = 1000

    for el in listEl:
        d = Levenshtein.distance(str(word), str(el))
        lenDis[el] = d

        if minDist > d:
            minDist = d

    minWords = extractListByDic(lenDis, minDist)

    return minWords


"""
Create data with len-key
"""
def createDataByLen(list):
    data = {}

    for el in list:
        if el != '':
            if not (len(el) in data.keys()):
                data[len(el)] = [el.lower()]
            else:
                data.get(len(el)).append(el.lower())

    return data

"""
Create file sorted json by data
"""
def sortedSavedJson(data, nameJson):
    od = collections.OrderedDict(sorted(data.items()))

    with open(nameJson, "w") as outfile:
        json.dump(od, outfile)

"""
Create list of bad words in order to clean the future model 
"""
def createListBadWords(path, nameFileMessages, nameFile):
    key = "bad"
    badWords = {key: []}

    with open(path + nameFileMessages) as f:
        dataMessages = json.load(f)

    with open(path + nameFile) as f:
        dataFile = json.load(f)

    for k in dataMessages.keys():
        for eachWord in dataMessages.get(k):
            if k in dataFile.keys():
                if not (eachWord in dataFile.get(k)):
                    badWords.get(key).append(eachWord)

    sortedSavedJson(badWords, "onlyBadWords.json")

"""
@:parameter messages: the name of the file, with the messages in html
@:parameter path: position of the files
@:parameter nameFileText: the name of the file where we save the messages
"""
def createFileWords(messages, path, nameFileText):
    for file in messages:
        soup = BeautifulSoup(open(path + '/' + file), "html.parser") #use soup for search and analyze the messages
        messagesFile = open(nameFileText, "w")
        for i, divText in enumerate(soup.findAll("div")): #save the name user and the messages, to divide later
            if divText.attrs.get('class')[0] == 'text' or divText.attrs.get('class')[0] == 'from_name':
                t = re.sub(r'(?<!\.)', '', divText.text)
                t = re.sub(r'       ', '', t)
                messagesFile.write(t + "\n")
    messagesFile.close()


"""
@:parameter nameFileText: the name of the file which we take the messages
@:parameter user1
@:parameter user2
In this methods we separate the message by user
"""
def createDocWords(nameFileText, user1, user2):
    setWords = {user1: [], user2: []}
    messagesFile = open(nameFileText, "r")
    messagesFun = messagesFile.readlines()
    sentenceFile = open("sentenceMessages.txt", "w")
    flag = 2
    for line in messagesFun:
        if user1 in line:
            flag = 0
        elif user2 in line:
            flag = 1
        else:
            if line != '' and line != '\n':
                #separate the message of user1 and user2
                if flag == 0:
                    setWords.get(user1).append(line)
                    sentenceFile.write(line + "\n")
                if flag == 1:
                    setWords.get(user2).append(line)
    messagesFile.close()

    return setWords


"""
@setUser: the set of messages by user
create the list, much as possible "clear"
"""
def createClearList(setUser, listToEliminateSymbols):
    listClearWords = []

    for word in setUser:
        #total split separate a word by blank / space and \n
        listClearWords = union(listClearWords, totalSplit(word))

    for el in listToEliminateSymbols:
        listClearWords = list(filter(lambda x: not (el in x), listClearWords))

    listClearWords = list(filter(lambda x: x !='', listClearWords))
    listClearWords = list(filter(lambda x: not (len(x) == 1), listClearWords))
    listClearWords = list(filter(lambda x: not (len(x) > 26), listClearWords))

    return listClearWords

"""
@:parameter word: the word to split
"""
def totalSplit(word):
    remove = string.punctuation
    pattern = r"[{}]".format(remove)  # create the pattern
    split = re.split('\n', word)
    blank = ""
    listWords = []
    for eachWord in split:
        eachWord = re.sub(pattern, "", eachWord)
        if eachWord != blank:
            clearList = re.split(' ', eachWord)
            listWords = union(listWords, clearList)

    return listWords

"""
By json extract the words
"""
def extractWordsByJson(path):
    data: dict
    listWords = []
    with open(path) as f:
      data = json.load(f)
    for k in data.keys():
        listWords = union(listWords, data.get(k))

    return listWords



def spellcheckerBaseLine(word, words_index, ntop=3):
    """ Restituisce i suggerimenti delle parole in base allo spellchecker creato da M.Atzori """
    from manage import ngramspell
    res = {
        "word": word,
        "suggestions":[ {w: {'score':score,'edit':edit}} for w, score, edit in ngramspell.similar2(words_index, word)[:ntop] ]
    }
    return res

def csvBaseLine(listBadWord, path_dizionario='', ntop=3, save = False, name='baseline.csv'):
    """creazione di un dataframe in formato csv, basato sullo spellchecker creato da M.Atzori"""
    from manage import ngramspell
    import pandas as pd
    words_index = ngramspell.index(path_dizionario)
    data_list = []
    for i in range(ntop):
        data_list.append([])

    for word in listBadWord:
        tmp = spellcheckerBaseLine(word, words_index, ntop)

        for i, k in enumerate(data_list):
            try:
                data_list[i].append(list(tmp['suggestions'][i].keys())[0])
            except IndexError:
                data_list[i].append('NaN')

    data = {'BadWord': listBadWord}

    for i, k in enumerate(data_list):
        data[f'Res_{i}'] = k

    df = pd.DataFrame(data)

    df.to_csv(name)

    return df,data_list
