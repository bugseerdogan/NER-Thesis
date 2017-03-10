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


tweet = "Eagles WR DeSean Jackson arrived at Philadelphia International Airport at about 8 p.m. on Sunday night, accompanied by Drew Rosenhaus:)"
word = "Philadelphia International Airport"
word2 = "Aiirport"
FindNumberOfWord(tweet, word)
hasPunctuation(word)
hasEmoticon(tweet)
hasConsecutive(tweet)