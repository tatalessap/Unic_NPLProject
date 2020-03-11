from bs4 import BeautifulSoup
import re
import os

"""
@:parameter messages: the name of the file, with the messages in html
@:parameter path: position of the files
@:parameter nameFileText: the name of the file where we save the messages
"""
def createFileWords(messages, path, nameFileText):
    for file in messages:
        soup = BeautifulSoup(open(path + file), "html.parser") #use soup for search and analyze the messages
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
                if flag == 1:
                    setWords.get(user2).append(line)
    messagesFile.close()
    return setWords

"""
@setUser: the set of messages by user
create the list, much as possible "clear"
"""
def createClearList(setUser):
    listClearWords = []

    for word in setUser:
        #total split separate a word by blank / space and \n
        listClearWords = union(listClearWords, totalSplit(word))

    listClearWords = list(filter(lambda a: a != '', listClearWords))

    return listClearWords

"""
@:parameter word: the word to split
"""
def totalSplit(word):
    split = re.split('\n', word)
    blank = ""
    listWords = []
    for eachWord in split:
        if eachWord != blank:
            clearList = re.split(' ', eachWord)
            listWords = union(listWords, clearList)
    return listWords


def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list
