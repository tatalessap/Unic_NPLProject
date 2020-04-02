from manage.corrector import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
from createFiles import createFiles
import os

#
import nltk
from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath
import numpy as np
import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#

pathTrain = '/home/tatalessap/PycharmProjects/Unic_NPLProject/sentenceMessages.txt'

pathModelW = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/WikiModelmono1epochS2.model'

pathModelF = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/2/WikiFast1bis.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile(pathFile):
    createFiles()

modelF = ModelFastText(pathModelF, True)

modelW = ModelWord2Vec(pathModelW, True)

f = 'per crsare questi messaggi non sto guardando lo schermo non ho idea di cosa sto scrivndo pernso di aver sbagliato qualche lettera'

print(f)

badWords, goodWords = checkSentence(pathFile, f)

print(getPossibleWords(modelW.predict, badWords, goodWords, "w2v"))

print(getPossibleWords(modelF.getSimilar, badWords, [], "ft"))