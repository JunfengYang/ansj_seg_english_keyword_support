#!/usr/bin/python
#-*- coding: utf-8 -*-

fo = open("sort","r")
rows = fo.read().split("\n")
fo.close()

words = set()

for row in rows:
    word = row.strip().lower()
    words.add(word)

words = list(words)
words.sort()

wf = open("aftersort","w")
for word in words:
    wf.write(word+"\n")
wf.close()