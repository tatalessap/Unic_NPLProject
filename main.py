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

nameFileWiki = "documents2.json"

user1 = 'Tata'

user2 = 'Stefano Raimondo Usa'

nameFileOutput = "Output.txt"

nameFileWordsCommon = "60000_parole_italiane.txt"

nameFileMessagesJson = 'wordsByLen.json'

nameFileWordsCommonJson = 'wordsByLenCommon.json'

nameFileWikiJson = 'wordsByLenWiki.json'

nameFileTotal = "totalWords.json"

listToEliminateSymbols = ['http', '/', '-', '😂', '\'', 'è', 'à', 'ù', 'ò']

#create a set by conversation by telegram
if not os.path.isfile(path+nameFileOutput):
    createFileWords(messages, path+pathMessages, nameFileOutput)
#create the doc
setWords = createDocWords(nameFileOutput, user1, user2)
#create a list by user (list of words)
clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

if not os.path.isfile(path+nameFileTotal):
    # if not exist, create a json with words order by their length
    if not os.path.isfile(path + nameFileMessagesJson):
        createFileJson(clearList, nameFileMessagesJson)

    if not os.path.isfile(path + nameFileWikiJson):
        createFileJson(extractWordsByJson(path+nameFileWiki), nameFileWikiJson)

    if not os.path.isfile(path + nameFileWordsCommonJson):
        createFileJson(createDocWordsText(path + nameFileWordsCommon), nameFileWordsCommonJson)
        sortedSavedJson(unionFileJson(path+nameFileWikiJson, path + nameFileWordsCommonJson), nameFileTotal)

createListBadWords(path, nameFileMessagesJson, nameFileTotal)

#createSetNotCorrectWords(path, nameFileMessagesJson, 'wordsByLenWiki.json')







