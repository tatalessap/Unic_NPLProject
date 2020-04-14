from manage.corrector import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
from createFiles import createFiles
import os
import pandas as pd
import numpy as np


#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#

pathTrain = '/home/tatalessap/PycharmProjects/Unic_NPLProject/sentenceMessages.txt'

pathModelW = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/W2CWikiITa2019ep5dim300neg10/WikiW2C300neg10ep5.model'

#pathModelF = '/home/tatalessap/PycharmProjects/Unic_NPLProject/models/FastTextWikiITa2019ep5dim300neg10/WikiFT300neg10ep5.model'

pathFile = '/home/tatalessap/PycharmProjects/Unic_NPLProject/totalWords.json'

if not os.path.isfile(pathFile):
    createFiles()

#modelF = ModelFastText(pathModelF, True)

print('modelf')

modelW = ModelWord2Vec(pathModelW, True)
print('modelw')

"""
sentence | bad word | correct word | baseline word | fasttext word | w2v word | chech correct word baseline | check correct word fasttext | check correct word word2vect
"""
#d = {'sentence': [], 'bad word': [], 'correct word': [], 'baseline': [], 'fasttext': [], 'word2vect': [], 'b': [], 'f': [], 'w2v': []}

d = {'sentence': [], 'bad word': [], 'correct word': [], 'word2vect': [], 'w2v': []}

setNotBadWords = []

with open("/home/tatalessap/PycharmProjects/Unic_NPLProject/sentenceMessages.txt") as file_in:
    bwords = open("BadWordaForBaseline.txt", "w")
    cwords = open("correction.txt", "w")


    for line in file_in:

        if((line != "\n") and (line != "     \n")) and len(line) > 5:

            badWords, goodWords = checkSentence(pathFile, line)

            if badWords != []:

                print("sentence:    " + line)

                for el in badWords:

                    if el not in setNotBadWords and el[0] != 'C:':

                        print("badwords    " + el)

                        # insert correct word
                        test4word = input("Insert correct word: ")

                        print(len(test4word))

                        if len(test4word) != 0 and len(test4word) != 1:
                            bwords.write(el + "\n")

                            cwords.write(test4word + "\n")

                            d.get('correct word').append(str(test4word))

                            d.get('sentence').append(line)

                            d.get('bad word').append(el)

                            pw = getPossibleWords(modelW.predict, str(el), goodWords, "w2v")

                            d.get('word2vect').append(getStringByList(pw))

                                #check if the word correct is in the list

                            d.get('w2v').append(test4word in pw)

                            pw.clear()

                            #pw = getPossibleWords(modelF.getSimilar, str(el), [], "ft")

                            #d.get('fasttext').append(getStringByList(pw))

                                # check if the word correct is in the list
                            #d.get('f').append(test4word in pw)
                        else:
                            setNotBadWords.append(el)
bwords.close()

cwords.close()

df = pd.DataFrame(data=d)

df.to_csv('prova1.csv')




