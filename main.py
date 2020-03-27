from manage.corrector import *
from manage.wordEmbeddings import *
from createFiles import createFiles
import os

pathModel = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/marta.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile('/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'):
    createFiles()

modelM = Model(pathModel, True)

f = 'Ciao, come stap'

print(f)

checkSentence(pathFile, f, modelM)






