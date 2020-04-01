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

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#

#pathModelW = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/martaWiki.model'

pathModelF = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/1/WikiFast1.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile(pathFile):
    createFiles()

modelF = FT_gensim.load(pathModelF)

sentences = datapath('/home/tatalessap/PycharmProjects/Unic_NPLProject/sentenceMessages.txt')

modelF.train(sentences, epochs=5, total_examples=modelF.corpus_count, compute_loss=False)

f = 'Hai finito di studiort?'

print(f)

badWords, goodWords = checkSentence(pathFile, f)

#getPossibleWordsByContext(modelW, badWords, goodWords)

getPossibleWordBySimilar(modelF, badWords)




