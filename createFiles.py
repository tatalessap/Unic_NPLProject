from manage.toManageData import *
import os

def createFiles():
    """
    Input to set, variables and name of files
    """
    pathGeneral = '/home/tatalessap/PycharmProjects/Unic_NPLProject/'

    folderWords = 'wordFiles/'

    folderMessages = 'messageFiles'

    nameFileWiki = "documents2.json"

    nameFileOutputByMessages = "allMessages.txt"

    nameFileWordsCommon = 'dizionario.txt'

    nameFileMessagesJson = 'wordsMessagesByLen.json'

    nameFileTotal = 'totalWords.json'

    user1 = 'Tata'

    user2 = 'Stefano Usai'

    listToEliminateSymbols = ['http', '/', '-', '😂', '\'', 'è', 'à', 'ù', 'ò']

    messages = os.listdir(pathGeneral+folderMessages)


    # create a set-words by conversation by telegram
    if not os.path.isfile(pathGeneral+nameFileTotal):
        createFileWords(messages, pathGeneral+folderMessages, nameFileOutputByMessages)

        # create the doc
        setWords = createDocWords(nameFileOutputByMessages, user1, user2)

        # create a list by user (list of words)
        clearList = createClearList(setWords.get(user1), listToEliminateSymbols)

        if not os.path.isfile(pathGeneral + nameFileTotal):

            dataWordsByMessages = createDataByLen(clearList) #data by messages

            sortedSavedJson(dataWordsByMessages, nameFileMessagesJson)

            #dataWordsByWiki = createDataByLen(extractWordsByJson(pathGeneral+folderWords+nameFileWiki)) #data by wikipedia

            dataWordsByCommon = createDataByLen(createDocWordsText(pathGeneral+folderWords+nameFileWordsCommon)) #data by common words

            #dataWordsByUnion = unionDataByData(dataWordsByWiki, dataWordsByCommon)

            dataWordsByUnion = dataWordsByCommon

            sortedSavedJson(dataWordsByUnion, nameFileTotal)

            createListBadWords(pathGeneral, nameFileMessagesJson, nameFileTotal)