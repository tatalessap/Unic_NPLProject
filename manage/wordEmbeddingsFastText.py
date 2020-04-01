import nltk
from pprint import pprint as print
from gensim.models.fasttext import FastText as FT_gensim
from gensim.test.utils import datapath
import numpy as np
import logging
import Levenshtein

def predict(model, word):
    print('ciao')
    most_similar = model.wv.most_similar(word, topn=10)  # parole simili dal modello
    print('ciao')
    dictionary = list(model.wv.vocab.keys())
    result = list(filter(lambda x: weight(word, x[0], x[1], dictionary), most_similar))  # filtro con la funzione weight

    result = {'prediction': result[:5]}  # dizionario con le prime 5 parole
    return result


def weight(word, similar_word, similarity, dictionary, constant = 0.5):

    word_len = 1 if len(word) <= 4 else 2 #se è minore di 4 è un articolo quasi sicuramente

    print('ciao')

    min_similarity = similarity > constant

    min_len = len(similar_word) > 4 #se è più lungo di 4 evito che siano articoli

    exist = 1 if word in dictionary else 0 # esiste nel dizionario?

    check_first_word = 1 if word[0] == similar_word[0] else 0 #controllo la prima lettera della parola

    levenshtein_distance = Levenshtein.ratio(word, similar_word) <= word_len

    #levenshtein_distance = nltk.edit_distance(word, similar_word) <= word_len #sostituire con quello di marta

    weight = word_len + min_similarity + min_len + exist + levenshtein_distance

    if weight > 3:
        return True
    else:
        return False