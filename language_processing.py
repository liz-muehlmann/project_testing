import nltk
import os

file = open(".\\txt\\106_KKGB_2020-01-10.txt", 'r')
for line in file:
    print(line.strip())