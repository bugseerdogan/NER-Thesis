import pandas as pd
import numpy as np
import re

def countVowels(string):
    vowel = ("aıioöuüAEIİOÖUÜ")
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    return count


def countCons(string):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    count = 0
    for i in string:
        if i in cons:
            count += 1
    return count

def hasPunctuation(word):
    words = []
    checker = 0
    for x in word.split(" "):
        words.append(x)

    # çoklu kelimeler icin kelimeleri ayirdik
    for y in range(0, len(words)):
        # sadece alfabetik karakter icerirse checker 1
        if (words[y].isalpha() == False):
            checker = 1
            break

    print("hasPunc:", checker)
    return checker

def hasEmoticon(word):
    emoticons = [':)', ':(', ';)', ':O', ':D', ':P', ':@', ':S', ':$', 'B)', ':\'(', ':*', '>:)', 'O:)', ':/', ':|',
                 ':B', ':SS', ':))', '8)', ':&', ':?', '<3', '(u)']
    checker = 0

    for i in range(0, len(emoticons)):
        if emoticons[i] in word:
            checker = 1
            break

    print("hasEmoticon:", checker)
    return checker

def hasVowel(word):
    vowel = ("aıioöuüAEIİOÖUÜ")
    hasVowel = 0
    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in vowel:
                hasVowel = 1

    return hasVowel

def hasConsonant(word):
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    hasCons=0

    for i in range(0, len(word) - 1):
        if (word[i] == word[i + 1]):
            if word[i] in cons:
                hasCons = 1
    return hasCons

def containNumber(tweet):
    cnt = 0
    digitLst = []
    wordLst = tweet.split(" ")
    for word in wordLst:
        if (word.isdigit()):
            digitLst.append(word)
        else:
            for i in range(len(word)):
                if(word[i].isdigit()):
                    digitLst.append(word[i])

    #print("Bu tweet %d tane rakam iceriyor" %len(digitLst))
    #for digit in digitLst:
        #print(digit)
    return len(digitLst)

def hasHashtag(tweet):

    wordLst = []
    wordLst = tweet.split(" ")
    hashtagLst = []
    i = 0
    for word in wordLst:
        if (word[0] == "#"):
            i = i + 1
            hashtagLst.append(word)

    if i > 0:
        #print("bu tweette %d adet hashtag var\nHashtagler:\n" % i)
        return hashtagLst

def hasUrl(tweet) :
    urlLst = re.findall(r'(https?://[^\s]+)', tweet)
    #print("Bu tweette %d adet url var" % len(urlLst))

    return urlLst;

def mostUsedWord(tweet):
    wordLst = tweet.split(" ")
    mostUsedWordInTweet = ""
    mostUsed = 0
    for i in range(len(wordLst)):
        cnt = 0
        for j in range(len(wordLst)):
            if(wordLst[i] == wordLst[j]):
                cnt = cnt + 1

        if(cnt > mostUsed):
            mostUsed = cnt
            mostUsedWordInTweet = wordLst[i]
    return mostUsedWordInTweet

#print("En cok kullanilan kelime:%s, %d kez tekrar edilmis" %(mostUsedWordInTweet, mostUsed))

def FindNumberOfWord(tweet, word):
    counter = []
    words_tweet = []
    words_tag = []
    #print(tweet)
    #print(word)

    # tweeti kelime kelime ayirdik
    for x in tweet.split(" "):
        words_tweet.append(x)

    # aranan etiketimizi kelimelere ayirdik
    for y in word.split(" "):
        words_tag.append(y)

    for i in range(0, len(words_tweet)):
        for j in range(0, len(words_tag)):
            if words_tweet[i] == words_tag[j]:
                counter.append(i + 1)

    #print("num of :", counter)
    return counter



def main():
    data = {
        'Word Before': [''],
        'WB Stem': [''],
        'WB POS Tag': [''],
        'WB Letter': [''],
        'WB Letter Diff Stem': [''],
        'WB Is Capital': [''],
        'WB Is All Capital': [''],
        'WB Has Punct BA': [''],
        'WB Has Emot BA': [''],
        'WB Has Double Consonant': [''],
        'WB Has Double Vowel': [''],
        'WB Has Harmony': [''],
        'WB Cons Vow Ratio': [''],
        'WB Contain Number': [''],
        'WB Has Hashtag': [''],
        'WB Has Url': [''],

        'Word': [''],
        'W Stem': [''],
        'W POS Tag': [''],
        'W Letter': [''],
        'W Letter Diff Stem': [''],
        'W Is Capital': [''],
        'W Is All Capital': [''],
        'W Has Punct BA': [''],
        'W Has Emot BA': [''],
        'W Has Double Consonant': [''],
        'W Has Double Vowel': [''],
        'W Has Harmony': [''],
        'W Cons Vow Ratio': [''],
        'W Contain Number': [''],
        'W Has Hashtag': [''],
        'W Has Url': [''],

        'Word After': [''],
        'WA Stem': [''],
        'WA POS Tag': [''],
        'WA Letter': [''],
        'WA Letter Diff Stem': [''],
        'WA Is Capital': [''],
        'WA Is All Capital': [''],
        'WA Has Punct BA': [''],
        'WA Has Emot BA': [''],
        'WA Has Double Consonant': [''],
        'WA Has Double Vowel': [''],
        'WA Has Harmony': [''],
        'WA Cons Vow Ratio': [''],
        'WA Contain Number': [''],
        'WA Has Hashtag': [''],
        'WA Has Url': [''],


        'Tweet' : [''],
        'Tweet including the word Has Punct BA' : [''],
        'Tweet including the word Has Punct BA' : [''],
        'Tweet including the word Has Hashtag' : [''],
        'Tweet including the word Has Mention' : [''],
        'Tweet including the word Has Url' : [''],
        'Frequently used word in Tweet' : [''],
        'Tweet FAV Ratio' : [''],
        'Tweet RT Ratio' : [''],
        'Tweet Has Location' : [''],
        'Tweet Has Checkin' : [''],
        'Tweet Sent From Mobile Device' : [''],
        'Length of tweet as # of words' : [''],
        'Length of tweet as # of characters' : [''],

    }

    words = []
    tweet=[]
    with open('1.txt', 'r') as f:
        for line in f:
            tweet.append(line)
            for word in line.split():
                words.append(word)

    df = pd.DataFrame(data, index=words)
    df2=pd.DataFrame(data, index=tweet)

    print('.....')
    """for i, row in df.iterrows():
        row['Word'] = i
        row['W Stem'] = i
        row['W POS Tag'] = 'X'
        row['W Letter'] = len(i)
        row['W Letter Diff Stem'] = len(i) - len(i)
        row['W Is Capital'] = i.istitle()
        row['W Is All Capital'] = i.isupper()
    print (df)
    """

    print('XXXX XXXX')

    for j in range(df.size):

        """ Word Before """
        df.iloc[j]['Word Before'] = df.index[j - 1]
        df.iloc[j]['WB Stem'] = df.index[j - 1]
        df.iloc[j]['WB POS Tag'] = 'X'
        df.iloc[j]['WB Letter'] = len(df.index[j - 1])
        df.iloc[j]['WB Letter Diff Stem'] = len(df.index[j - 1]) - len(df.index[j - 1])
        df.iloc[j]['WB Is Capital'] = df.index[j - 1].istitle()
        df.iloc[j]['WB Is All Capital'] = df.index[j - 1].isupper()
        df.iloc[j]['WB Has Punct BA'] = hasPunctuation(df.index[j - 1])
        df.iloc[j]['WB Has Emot BA'] = hasEmoticon(df.index[j - 1])
        df.iloc[j]['WB Has Double Consonant'] = hasConsonant(df.index[j - 1])
        df.iloc[j]['WB Has Double Vowel'] = hasVowel(df.index[j - 1])
        df.iloc[j]['WB Has Harmony'] = ''
        df.iloc[j]['WB Contains Number'] = containNumber(df.index[j - 1])
        df.iloc[j]['WB Has Hashtag'] = hasHashtag(df.index[j - 1])
        df.iloc[j]['WB Has Url'] = hasUrl(df.index[j - 1])
        if (countVowels(df.index[j - 1]) > 0):
            df.iloc[j]['WB Cons Vow Ratio'] = countCons(df.index[j - 1]) / countVowels(df.index[j - 1])
        else:
            df.iloc[j]['WB Cons Vow Ratio'] = 0


        """ Word """
        df.iloc[j]['Word'] = df.index[j]
        df.iloc[j]['W Stem'] = df.index[j]
        df.iloc[j]['W POS Tag'] = 'X'
        df.iloc[j]['W Letter'] = len(df.index[j])
        df.iloc[j]['W Letter Diff Stem'] = len(df.index[j]) - len(df.index[j])
        df.iloc[j]['W Is Capital'] = df.index[j].istitle()
        df.iloc[j]['W Is All Capital'] = df.index[j].isupper()
        df.iloc[j]['W Has Punct BA'] = hasPunctuation(df.index[j])
        df.iloc[j]['W Has Emot BA'] = hasEmoticon(df.index[j])
        df.iloc[j]['W Has Double Consonant'] = hasConsonant(df.index[j])
        df.iloc[j]['W Has Double Vowel'] = hasVowel(df.index[j])
        df.iloc[j]['W Has Harmony'] = ''
        df.iloc[j]['W Contains Number'] = containNumber(df.index[j])
        df.iloc[j]['W Has Hashtag'] = hasHashtag(df.index[j])
        df.iloc[j]['W Has Url'] = hasUrl( df.index[j])
        if (countVowels(df.index[j]) > 0):
            df.iloc[j]['W Cons Vow Ratio'] = countCons(df.index[j]) / countVowels(df.index[j])
        else:
            df.iloc[j]['W Cons Vow Ratio'] = 0

        """ Word After """
        df.iloc[j]['Word After'] = df.index[j + 1]
        df.iloc[j]['WA Stem'] = df.index[j + 1]
        df.iloc[j]['WA POS Tag'] = 'X'
        df.iloc[j]['WA Letter'] = len(df.index[j + 1])
        df.iloc[j]['WA Letter Diff Stem'] = len(df.index[j + 1]) - len(df.index[j + 1])
        df.iloc[j]['WA Is Capital'] = df.index[j + 1].istitle()
        df.iloc[j]['WA Is All Capital'] = df.index[j + 1].isupper()
        df.iloc[j]['WA Has Punct BA'] = hasPunctuation(df.index[j + 1])
        df.iloc[j]['WA Has Emot BA'] = hasEmoticon(df.index[j + 1])
        df.iloc[j]['WA Has Double Consonant'] = hasConsonant(df.index[j + 1])
        df.iloc[j]['WA Has Double Vowel'] = hasVowel(df.index[j + 1])
        df.iloc[j]['WA Has Harmony'] = ''
        df.iloc[j]['WA Contains Number'] = containNumber(df.index[j + 1])
        df.iloc[j]['WA Has Hashtag'] = hasHashtag(df.index[j + 1])
        df.iloc[j]['WA Has Url'] = hasUrl(df.index[j + 1])
        if (countVowels(df.index[j + 1]) > 0):
            df.iloc[j]['WA Cons Vow Ratio'] = countCons(df.index[j + 1]) / countVowels(df.index[j + 1])
        else:
            df.iloc[j]['WA Cons Vow Ratio'] = 0

        if (j == 370):
            break
    for i in range(df2.size):
        """Tweet"""
        df2.iloc[j]['Tweet including the word Has Punct BA'] =hasPunctuation(df2.index[i])
        df2.iloc[j]['Tweet including the word Has Punct BA'] = hasEmoticon(df2.index[i])
        df2.iloc[j]['Tweet including the word Has Hashtag'] = hasHashtag(df2.index[i])
        df2.iloc[j]['Tweet including the word Has Mention'] = ''
        df2.iloc[j]['Tweet including the word Has Url']=hasUrl(df2.index[i])
        df2.iloc[j]['Frequently used word in Tweet'] =mostUsedWord(df2.index[i])
        df2.iloc[j]['Tweet FAV Ratio'] = ''
        df2.iloc[j]['Tweet RT Ratio'] = ''
        df2.iloc[j]['Tweet Has Location'] = ''
        df2.iloc[j]['Tweet Has Checkin'] = ''
        df2.iloc[j]['Tweet Sent From Mobile Device'] = ''
        df2.iloc[j]['Length of tweet as # of words'] = FindNumberOfWord(df2.index[i],df.index[j])
        df2.iloc[j]['Length of tweet as # of characters'] = ''


    print(df)

    print('.....')


main()