# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import re
import csv
import collections

def main():
    rows = []
    array_dic = []
    array_class = []
    f = open('tweet1_2304.csv', 'rt')
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
    finally:
        f.close()
    for i in range(0,len(rows)):

        if (rows[i] != []):
            dic = dict()
            dic['word'] = rows[i][2]

            array_dic.append(dic)
            array_class.append(rows[i][3])

    from sklearn.feature_extraction import DictVectorizer
    vec = DictVectorizer()
    train_vector = vec.fit_transform(array_dic)

    # 1. METHOD: LOGISTIC REGRESSION
    #from sklearn.linear_model.logistic import LogisticRegression
    #train_model = LogisticRegression()
    #train_model.fit(train_vector, array_class)

    from sklearn.naive_bayes import MultinomialNB
    train_model = MultinomialNB()
    train_model.fit(train_vector, array_class)

    lines_test= []
    f = open('test.csv', 'rt')
    try:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            lines_test.append(row)
    finally:
        f.close()

        array_dic_test = []
        test_class = []
        for i in range(0, len(lines_test)):

            if (lines_test[i] != []):
                dic_test = dict()
                dic_test['word'] = lines_test[i][2]
                array_dic_test.append(dic_test)
                test_class.append(lines_test[i][3])

        test_vector = vec.transform(array_dic_test)

        # PREDICT CLASS
        predicted = []
        predicted = train_model.predict(test_vector)

    from sklearn.metrics import classification_report
    print(classification_report(test_class, predicted, target_names=list(set(test_class))))

    print('.....')

main()