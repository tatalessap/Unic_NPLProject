from manage.corrector import *
from manage.wordEmbeddingsWord2Vec import *
from manage.wordEmbeddingsFastText import *
from createFiles import createFiles
import os
import pandas as pd
import numpy as np
"""
call of the main methods and comparison with the two models
"""

pathTrain = ''

pathModelW = ''

pathModelF = ''

pathFile = ''

if not os.path.isfile(pathFile):
    createFiles() #create the necessary files, set of messages and dictionary


if not os.path.isfile('not_filtered.csv'): #if not are the list of bad sentence, create one with
        d = {'sentence': [], 'bad word': []} #the sentence and the bad words

        count = 0

        setNotBadWords = []

        flag = True

        with open("/home/tatalessap/PycharmProjects/Unic_NPLProject/setMessages.json") as js: #open a list of sentence by utent

            jListM = json.load(js)

            listM = jListM.get('') #insert utent name

            for line in listM:

                if flag:

                    if((line != "\n") and (line != "     \n")) and (len(line) > 5 and len(line)< 50) and 'www' not in line:

                        badWords, goodWords = checkSentence(pathFile, line)

                        if badWords != []:

                            for el in badWords:

                                if (el not in setNotBadWords) and (len(el) > 4) and ('ah'not in el and 'eh' not in el and 'mmh' not in el):
                                    count = count + 1
                                    print("badwords    " + el)

                                    d.get('sentence').append(line)

                                    d.get('bad word').append(el)

                                    if count == 300:
                                        flag = False


        df = pd.DataFrame(data=d)

        df.to_csv('not_filtered.csv')

#filtered the sentence and add a new coloumn with the correct words.

df = pd.read_csv('filtered.csv') #this file was done externally to the code

listS = df.get('sentence')

listBW = df.get('bad word')

listCW = (df.get('Unnamed: 3')) #column of correct words


#word2vect

if not os.path.isfile('docW2V.csv'):

    d = {'sentence': [], 'bad word': [], 'correct word': [], 'word2vect': [], 'w2v': []}

    modelW = ModelWord2Vec(pathModelW, True)
    print('modelw')

    ind = 0

    for b in listBW:

        d.get('sentence').append(listS.get(ind))

        d.get('bad word').append(b)

        d.get('correct word').append(listCW.get(ind))

        goodWords = getGoodWord(pathFile, listS.get(ind))

        pw = getPossibleWords(modelW.predict, str(b), goodWords, "w2v")

        if listCW.get(ind) in (list(map(lambda x: x[0], pw))):

            d.get('w2v').append(1)
        else:
            d.get('w2v').append(0)

        d.get('word2vect').append(getStringByList(pw))

        pw.clear()

        ind = ind + 1

    df = pd.DataFrame(data=d)

    df.to_csv('docW2V.csv')

###
d = {'fasttext': [], 'ft': []}

modelF = ModelFastText(pathModelF, True)

print('modelf')

ind = 0
d = {'fasttext': [], 'ft': []}

modelF = ModelFastText(pathModelF, True)

print('modelf')

ind = 0

for b in listBW:

    pw = getPossibleWords(modelF.getSimilar, str(b), b, "ft")

    if listCW.get(ind) in (list(map(lambda x: x[0], pw))):
        d.get('ft').append(1)
    else:
        d.get('ft').append(0)

    d.get('fasttext').append(getStringByList(pw))

    pw.clear()

    ind = ind + 1

df = pd.DataFrame(data=d)

df.to_csv('docFT.csv')

