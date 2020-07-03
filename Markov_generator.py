from urllib.request import urlopen
from bs4 import BeautifulSoup

# text = str(urlopen('url').read(), 'utf-8')

# wordDict = BuildWordDict(text)
text =  "I said to him him I said I said said "

def BuildWordDict(text):
    # cleaning removing quites , putting spaces
    #  formatting
    #  build a 2d array dic of dic of the form:- 

    #  a --> 50% b 
    # a ---> 25% c and d 

    """{word_a : {word_b : 2, word_c : 1, word_d : 1},
        word_e : {word_b : 5, word_d : 2},...}
    """


    text =text.replace("\n", " ")
    text =text.replace("\ ", " ")
    punctuations = [",", ".", ";", "!", "?" ,"!", "@"]
    for symbol in punctuations:
        text = text.replace(symbol, " "+symbol+" ")
        # He asked him, go there! ----> He asked him__,__go there__!__
    
    words = text.split(" ")
    # print(words) a list of words
    words = [word for word in words if word !="" or word !=""]
    print(words)

    wordDict = {}
    # words =  [I , said ,to,  him, him ,I ,said, I, said, said ]

    for i in range(1, len(words)):
        wordDict[words[i-1]] =  {}
        if words[i] not in wordDict[words[i-1]]:
            # wordDict[words[i-1]][words[i]] = 0
            wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
    print(wordDict)

BuildWordDict(text)
