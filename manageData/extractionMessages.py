from bs4 import BeautifulSoup
import re


def createSetWords(messages, path, user1, user2):
    setWords = {user1: [], user2: []}

    for file in messages:
        soup = BeautifulSoup(open(path + file), "html.parser")

        for i, divText in enumerate(soup.findAll("div")):
            if user1 in divText.text:
                setWords.get(user1).append(divText.text)
            elif user2 in divText.text:
                setWords.get(user2).append(divText.text)
    return setWords

"""
def createClearList(set):
    listClearWords = []

    for word in set:
        listClearWords = union(listClearWords, (word.split(" ")))
        listClearWords = union(listClearWords, (word.split("\n")))

    listClearWords = list(filter(lambda a: a != '', listClearWords))

    return listClearWords

def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list
"""