from bs4 import BeautifulSoup
import re


def createSetWords(messages, path, user1, user2):
    setWords = {user1: [], user2: []}
    flag = 0
    for file in messages:
        soup = BeautifulSoup(open(path + file), "html.parser")

        for i, div in enumerate(soup.findAll("div")):

            if user1 in div.text:
                flag = 1
            if user2 in div.text:
                flag = 0

            t = re.sub(r'(?<!\.)\n', '', div.text)
            t = re.sub(r'       ', '', t)
            if div.attrs.get('class')[0] == 'text':
                setWords.get(user1).append(t) if flag == 1 else setWords.get(user1).append(t)

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