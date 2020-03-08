import os
from manageData.toCreateSetWords import *

#list of messages, for example messages2.html
messages = os.listdir('/home/tatalessap/PycharmProjects/NPLProject/Files')

pathMessages = "/home/tatalessap/PycharmProjects/Prova1/ChatExport_02_03_2020/"

user1 = 'Marta Pibiri'

user2 = 'Stefano Raimondo Usa'

listRemoveElements = ['MP', 'S']

nameFileText = "Output.txt"

#createFileWords(messages, pathMessages, nameFileText)

setWords = createDocWords(nameFileText, user1, user2)

clearList = createClearList(setWords.get(user1), listRemoveElements)

wordsFile = open("Words.txt", "w")
for el in clearList:
    wordsFile.write(el + "\n")
wordsFile.close()

