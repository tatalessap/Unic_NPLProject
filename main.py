from manage.corrector import *
from manage.wordEmbeddings import *
from createFiles import createFiles
import os

pathModel = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/marta.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile(pathFile):
    createFiles()

modelM = Model(pathModel, True)

f = 'Ciao, non cipito perché non mi ripondi'

print(f)

checkSentence(pathFile, f, modelM)

dct = {'ciao': 1, 'ciauP' : 4, 'uncis': 4}





