from bs4 import BeautifulSoup
import re

def createSetWords(messages, path, user1, user2):
    setWords = {user1: [], user2: []}

    for file in messages:
        soup = BeautifulSoup(open(path + file), "html.parser")

        for i, divText in enumerate(soup.findAll("div")):
            if user1 in divText.text:
                setWords.get(user1).append(divText.text)
            elif user2 in divText.text:
                setWords.get(user2).append(divText.text)
    return setWords

def createClearList(set):
    listClearWords = []

    for word in set:
        listClearWords = union(listClearWords, totalSplit(word))
        l#istClearWords = list(filter(lambda a: a != '', listClearWords))
        #listClearWords = list(filter(lambda a: a != [1-2], listClearWords))
        i = 0

    return listClearWords

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

def totalSplit(word):
    split = re.split('\n', word)
    blank = ""
    listWords = []
    for eachWord in split:
        if eachWord != blank:
            clearList = re.split(' ', eachWord)
            listWords = union(listWords, clearList)
    return listWords