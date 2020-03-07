import os
from manageData.extractionMessages import *
import manageData.extractionMessages

#list of messages, for example messages2.html
messages = os.listdir('/home/tatalessap/PycharmProjects/NPLProject/Files')

path = "/home/tatalessap/PycharmProjects/Prova1/ChatExport_02_03_2020/"

user1 = 'Marta Pibiri'

user2 = 'Stefano Raimondo Usa'

setWords = createSetWords(messages, path, user1, user2)

u = 0

"""
listClearWords = createClearList(setWords.get(user1))
print(listClearWords)
"""


