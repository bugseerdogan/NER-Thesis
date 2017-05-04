# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


searchfile = open("deneme_text.txt", "r")
for line in searchfile:
    if "Percent" in line:
        print line
searchfile.close()