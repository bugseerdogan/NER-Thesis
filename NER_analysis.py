# -*- coding: utf-8 -*-
# encoding=utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import collections
def main():
    rows = []
    f = open('tweet1_2304.csv', 'rt')
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    finally:
        f.close()

    counter = 1
    list = []
    for i in range(1, len(rows)):
        if (rows[i][1] == rows[i - 1][1]):
            counter += 1
        else:
            list.append(counter)
            counter = 1

    # tweets[0]="id,tweet,word,tag" , list[0]=1
    # tweets[1],list[1]=3    0,3
    # tweets[4],list[2]=6    3,9
    # tweets[10],list[3]=3   9,12
    # tweets[13],list[4]=8   12,20

    index = 1
    index2 = 0
    words = []
    taglist = []
    tweetlist=[]
    for j in range(1, len(list)):

        index += list[j]
        tweetlist.append(rows[index-1][1])
        start = index2
        index2 += list[j]
        end = index2
        for word in rows[index - 1][1].split():
            tag = []
            # list(i-1),list(i-1)+list(i)
            for i in range(start, end):
                if word == rows[i + 1][2]:
                    tag.append(rows[i + 1][3])
                else:
                    tag.append('Other')

            counter = collections.Counter(tag)
            if counter.__len__() == 1:
                # print word,'Other'
                words.append(word)
                taglist.append('Other')
            else:
                tagx = counter.items().pop(0)
                words.append(word)
                taglist.append(tagx[0])
                # print word,tagx[0]


    #df = pd.DataFrame(data, index=words)
    #df2=pd.DataFrame(data2, index=tweetlist)
'''
rows =[]
f = open('filteredlist.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
finally:
    f.close()
'''

df = pd.read_csv('test.csv' , names=['id', 'tweet', 'word', 'tagType'])

personCount , locationCount , organizationCount, productCount= 0,0,0,0
dateCount , moneyCount , percentCount ,otherCount= 0,0,0,0



for i in range(0, len(df) - 1):
    if df.tagType[i] == 'Person':
        personCount += 1
    elif df.tagType[i] == 'Location':
        locationCount += 1
    elif df.tagType[i] == 'Organization':
        organizationCount += 1
    elif df.tagType[i] == 'Product':
        productCount += 1
    elif df.tagType[i] == 'Date':
        dateCount += 1
    elif df.tagType[i] == 'Money':
        moneyCount += 1
    elif df.tagType[i] == 'Percent':
        percentCount += 1
    else:
        otherCount += 1

tagTypes = ['Person' , 'Location' , 'Organization' , 'Product' , 'Date' , 'Money' , 'Percent']


counter = [personCount, locationCount,organizationCount, productCount,dateCount, moneyCount,percentCount]
list = {'tagTypes':tagTypes,'counter': counter}
df_taglist =pd.DataFrame(list)

print df_taglist

print "***Max value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== max(df_taglist.counter)].index]

print "\n***Min value of tagged value: " ,df_taglist.tagTypes[df_taglist[df_taglist['counter']== min(df_taglist.counter)].index]

print "\n***Mean of tagged word:",df_taglist.mean()

print "\n***Standart deviation of tagged word:",df_taglist.std()


N=7
## necessary variables
ind = np.arange(N)  # the x locations for the groups
width = 0.25  # the width of the bars
menStd = [0, 0, 0, 0, 0, 0, 0]

fig = plt.figure()
ax = fig.add_subplot(111)
rects4 = ax.bar(ind, counter, width,color='purple',yerr=menStd, error_kw=dict(elinewidth=7, ecolor='red'))

# axes and labels
ax.set_xlim(-width, len(ind) + width)
ax.set_ylim(0, max(df_taglist.counter)+100)
ax.set_title('Class Histogram of Test Data')
xTickMarks = ['Person','Location','Organization', 'Product','Date','Money','Percent']
ax.set_xticks(ind + width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames,color='black', rotation=45, fontsize=10)

plt.show()
main()