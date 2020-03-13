import os
import json
from manageData.toCreateSetWords import *
from manageData.toManageData import *
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

listToEliminateSymbols = ['http', '/', '-', '😂', '\'', 'è', 'à', 'ù', 'ò']

##

if not os.path.isfile("/home/tatalessap/PycharmProjects/NPLProject/"+nameFileText):
    createFileWords(messages, pathMessages, nameFileText)

setWords = createDocWords(nameFileText, user1, user2)

clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

createFileJson(clearList)

with open('/home/tatalessap/PycharmProjects/NPLProject/wordsByLen.json') as f:
  data = json.load(f)


"""

maxiMatrixSim = createMatrixSimByDic(data)

sortedSavedJson(maxiMatrixSim, 'matrixSim.json')

"""



i = 0

"""
wordsFile = open("Words.txt", "w")
for el in clearList:
    wordsFile.write(el + "\n")
wordsFile.close()
"""




