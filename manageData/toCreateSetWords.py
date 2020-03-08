from bs4 import BeautifulSoup
import re


def createFileWords(messages, path, nameFileText):
    for file in messages:
        soup = BeautifulSoup(open(path + file), "html.parser")
        messagesFile = open(nameFileText, "w")
        for i, divText in enumerate(soup.findAll("div")):
            messagesFile.write(divText + "\n")
        messagesFile.close()


def createDocWords(nameFileText, user1, user2):
    setWords = {user1: [], user2: []}
    messagesFile = open(nameFileText, "r")
    messagesFun = messagesFile.readlines()
    flag = 2
    for line in messagesFun:
        if user1 in line:
            flag = 0
        elif user2 in line:
            flag = 1
        else:
            if line != '' and line != '\n':
                if flag == 0:
                    setWords.get(user1).append(line)
                if flag == 1:
                    setWords.get(user2).append(line)
    messagesFile.close()
    return setWords


def createClearList(set, listRemoveElements):
    listClearWords = []

    for word in set:
        listClearWords = union(listClearWords, totalSplit(word))

    listClearWords = list(filter(lambda a: a != '', listClearWords))
    for ele in listRemoveElements:
        listClearWords = list(filter(lambda a: a != ele, listClearWords))

    return listClearWords


def totalSplit(word):
    split = re.split('\n', word)
    blank = ""
    listWords = []
    for eachWord in split:
        if eachWord != blank:
            #eachWord = re.sub(r'(?<!\.)', ' ', eachWord)
            clearList = re.split(' ', eachWord)
            listWords = union(listWords, clearList)
    return listWords

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list