import re

def FindNumberOfWord(tweet, word):
    counter = []
    words_tweet = []
    words_tag = []
    print(tweet)
    print(word)

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

    print("num of :", counter)
    return counter


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

def hasEmoticon(tweet):
    emoticons = [':)', ':(', ';)', ':O', ':D', ':P', ':@', ':S', ':$', 'B)', ':\'(', ':*', '>:)', 'O:)', ':/', ':|',
                 ':B', ':SS', ':))', '8)', ':&', ':?', '<3', '(u)']
    checker = 0

    for i in range(0, len(emoticons)):
        if emoticons[i] in tweet:
            checker = 1
            break

    print("hasEmoticon:", checker)
    return checker

def hasConsecutive(tweet):
    vowel = ("aıioöuüAEIİOÖUÜ")
    cons = ("bcçdfgğhjklmnprsştyzBCÇDFGĞHJKLMNPRSŞTVYZ")
    hasVowel = 0
    hasCons =0
    for i in range(0, len(tweet) - 1):
        if (tweet[i] == tweet[i + 1]):
            if tweet[i] in vowel:
                hasVowel= 1
            elif tweet[i] in cons:
                hasCons= 1

    print("has Vowel?:",hasVowel)
    print("has Cons?:", hasCons)


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
        print("bu tweette %d adet hashtag var\nHashtagler:\n" % i)
        for hashtag in hashtagLst:
            print(hashtag)
    else:
        print("Bu tweette hashtag yok!")


def hasUrl(tweet) :
    urlLst = re.findall(r'(https?://[^\s]+)', tweet)
    print("Bu tweette %d adet url var" % len(urlLst))
    for url in urlLst:
        print(url)


def isNotWord(word):
    urlLst = re.findall(r'(https?://[^\s]+)', word)
    if len(urlLst) > 0 :
        return True

    if word[0] == "#":
        return True

    if word[:4] == "pic.":
        return True

    return False

def lengthOfTweet(tweet) :
    wordLst = []
    tweetWordLst = tweet.split(" ")
    for word in tweetWordLst:
        if not (isNotWord(word)):
            wordLst.append(word)


    print("Bu tweette %d adet sozcuk var" %len(wordLst))
    for word in wordLst:
        print(word)


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

    print("Bu tweet %d tane rakam iceriyor" %len(digitLst))
    for digit in digitLst:
        print(digit)


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


    print("En cok kullanilan kelime:%s, %d kez tekrar edilmis" %(mostUsedWordInTweet, mostUsed))





tweet = "Eagles WR DeSean Jackson arrived at Philadelphia International Airport at about 8 p.m. Sunday night, accompanied by Drew Rosenhaus:) #travel https://twitter.com/ pic.twitter.com/fMsmGoHYGV"
#word = "Philadelphia International Airport"
#word2 = "Aiirport"
#FindNumberOfWord(tweet, word)
#hasPunctuation(word)
#hasEmoticon(tweet)
#hasConsecutive(tweet)

#hasHashtag(tweet)
#hasUrl(tweet)
#lengthOfTweet(tweet)
#containNumber(tweet)
mostUsedWord(tweet)