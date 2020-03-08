import os
from manageData.extractionMessages import *
import manageData.extractionMessages
import time

#list of messages, for example messages2.html
messages = os.listdir('/Users/stefanoraimondousai/Documents/ReadingCourse/Unic_NPLProject/Files')
start= time.time()
path = "/Users/stefanoraimondousai/Documents/ReadingCourse/Unic_NPLProject/Files/"

user1 = 'Marta Pibiri'

user2 = 'Stefano Raimondo Usa'

setWords = createSetWords(messages, path, user1, user2)

u = 0
end=time.time()


print(setWords.get(user1))
print(end-start)
"""
listClearWords = createClearList(setWords.get(user1))
print(listClearWords)
"""


