import os
import json
from manage.toCreateSetWords import *
from manage.toManageData import *


"""
Input to set, variables and name of files
"""
#list of messages, for example messages2.html
path = '/home/tatalessap/PycharmProjects/NPLProject/'

pathMessages = 'Files'

messages = os.listdir(path+pathMessages)

fileWiki = "documents.json"

user1 = 'Tata'

user2 = 'Stefano Raimondo Usa'

fileNameTextOut = "Output.txt"

listToEliminateSymbols = ['http', '/', '-', '😂', '\'', 'è', 'à', 'ù', 'ò']

if not os.path.isfile(path+fileNameTextOut):
    createFileWords(messages, path+pathMessages, fileNameTextOut)

setWords = createDocWords(fileNameTextOut, user1, user2)

clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

nameFileMessages = 'wordsByLen.json'

if not os.path.isfile(path+nameFileMessages):
    createFileJson(clearList, 'wordsByLen.json')

wikiList = extractWordsByJson(path+fileWiki)

nameFileWiki = 'wordsByLenWiki.json'

if not os.path.isfile(path+'wordsByLenWiki.json'):
    createFileJson(wikiList, 'wordsByLenWiki.json')

createSetNotCorrectWords(path, nameFileMessages, nameFileWiki)





