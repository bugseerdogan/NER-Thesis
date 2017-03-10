def FindNumberOfWord(tweet, word):
    counter= []
    words_tweet =[]
    words_tag =[]
    print(tweet)
    print(word)

    #tweeti kelime kelime ayirdik
    for x in tweet.split(" "):
        words_tweet.append(x)

    #aranan etiketimizi kelimelere ayirdik
    for y in word.split(" "):
        words_tag.append(y)

    for i in range(0, len(words_tweet)):
        for j in range(0, len(words_tag)):
            if words_tweet[i] == words_tag[j]:
                counter.append(i+1)

    print("num of :",counter)
    return counter

def hasPunctuation(word):
    words =[]
    checker =[]
    count =0
    for x in word.split(" "):
        words.append(x)

    #coklu kelimeler icin kelimeleri ayirdik
    for y in range(0, len(words)):
        #sadece alfabetik karakter icerirse checker 0
        if(words[y].isalpha()):
            checker.append(0)
        #alfabetik karakterden baska seyler de varsa checker 1
        else:
            checker.append(1)

    print("hasPunc:",checker)

tweet = "Eagles WR DeSean Jackson arrived at Philadelphia International Airport at about 8 p.m. on Sunday night, accompanied by Drew Rosenhaus"
word = "Philadelphia International Airport"
word2 = "Phi+32ladelphia International Airport"
FindNumberOfWord(tweet, word)
hasPunctuation(word2)
