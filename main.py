import os
from manageData.toCreateSetWords import *
"""
Input to set, variables and name of files
"""
#list of messages, for example messages2.html
pathMessages = '/home/tatalessap/PycharmProjects/NPLProject/Files'

messages = os.listdir(pathMessages)

pathMessages = "/home/tatalessap/PycharmProjects/NPLProject/Files"

user1 = 'Tata'

user2 = 'Stefano Raimondo Usa'

nameFileText = "Output.txt"

listToEliminateSymbols = ['http', '/', '-', '😂']

##

if not os.path.isfile("/home/tatalessap/PycharmProjects/NPLProject/"+nameFileText):
    createFileWords(messages, pathMessages, nameFileText)

setWords = createDocWords(nameFileText, user1, user2)

clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

wordsFile = open("Words.txt", "w")
for el in clearList:
    wordsFile.write(el + "\n")
wordsFile.close()




