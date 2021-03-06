from manage.toManageData import *
import os

def createFiles():
    """
    Input to set, variables and name of files
    """
    pathGeneral = ''

    folderWords = 'wordFiles/'

    folderMessages = 'messageFiles'

    nameFileWiki = "documents2.json"

    nameFileWordsCommon = '660000_parole_italiane.txt'

    nameFileMessagesJson = 'wordsMessagesByLen.json'

    nameFileTotal = 'totalWords.json'

    user1 = ''  #insert name of utent in the messages

    user2 = ''

    listToEliminateSymbols = ['http', '/', '-', '😂', '\'', 'è', 'à', 'ù', 'ò']

    messages = os.listdir(pathGeneral+folderMessages)


    # create a set-words by conversation by telegram
    if not os.path.isfile(pathGeneral+nameFileTotal):

        # create the doc
        setWords = createDocWords(messages, pathGeneral+folderMessages, user1, user2)

        with open("setMessages.json", "w") as outfile:
            json.dump(setWords, outfile)

        # create a list by user (list of words)
        clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

        if not os.path.isfile(pathGeneral + nameFileTotal):

            dataWordsByMessages = createDataByLen(clearList) #data by messages

            sortedSavedJson(dataWordsByMessages, nameFileMessagesJson)

            dataWordsByWiki = createDataByLen(extractWordsByJson(pathGeneral+folderWords+nameFileWiki)) #data by wikipedia

            dataWordsByCommon = createDataByLen(createDocWordsText(pathGeneral+folderWords+nameFileWordsCommon)) #data by common words

            dataWordsByUnion = unionDataByData(dataWordsByWiki, dataWordsByCommon)

            sortedSavedJson(dataWordsByUnion, nameFileTotal)

            createListBadWords(pathGeneral, nameFileMessagesJson, nameFileTotal)