import os
from manageData.extractionMessages import *
import time
import json

messages = os.listdir('Files')
start= time.time()
path = "Files/"

user1 = 'Marta Pibiri'

user2 = 'Stefano Raimondo Usa'

setWords = createSetWords(messages, path, user1, user2)

u = 0
end=time.time()
print(end-start)
if not (os.path.exists('Documents/')):
    os.mkdir('Documents')

with open('Documents/documents.json', 'w') as outfile:
    json.dump(setWords, outfile)

