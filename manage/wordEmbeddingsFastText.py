import nltk
from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath
import numpy as np
import Levenshtein

class ModelFastText:
    def __init__(self, path, existModel=False):
        if existModel:
            self.loadModel(path)
        else:
            self.createModel(path)

    def createModel(self, pathTrain, size=300, min_count=50, sg=1, workers=8, progress_per=50000):
        self.model = FT_gensim(size=300, min_count=50, sg=1, workers=8)
        sentences = datapath(pathTrain)
        self.model.build_vocab(corpus_file=sentences, progress_per=50000)

    def loadModel(self, path):

        self.model = FT_gensim.load(path)

    def trainModel(self, pathTrain, epochs=5, compute_loss=False):
        sentences = datapath(pathTrain)

        self.model.train(sentences, epochs=5, total_examples=self.model.corpus_count, compute_loss=False)

    def saveModel(self, nameFile):
        self.model.save(nameFile+".model")

    def getSimilar(self, word):
        return self.model.wv.most_similar(word, topn=50)