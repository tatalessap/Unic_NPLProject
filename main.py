from manage.corrector import *
from manage.wordEmbeddings import *
from createFiles import createFiles
import os

pathModel = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/martaWiki.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile(pathFile):
    createFiles()

modelM = Model(pathModel, True)

f = 'Hai finito di studiort?'

print(f)

print("uno")

sentenceList = checkSentence2(pathFile, f, modelM, softness=0)

modelM.trainMoreSentence(sentenceList)