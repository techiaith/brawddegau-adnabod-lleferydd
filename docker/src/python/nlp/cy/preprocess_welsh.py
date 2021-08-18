import re

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def clean(sentence):
    sentence = sentence.replace('\u2013',"-")
    sentence = sentence.replace('\u2014',"-")
    sentence = sentence.replace('\uFE58',"-")
    sentence = sentence.replace('\u2018',"'")
    sentence = sentence.replace('\u2019',"'")
    sentence = sentence.replace("\u201C","\"")
    sentence = sentence.replace("\u201D","\"")
    sentence = sentence.replace('ñ',"n")
    return sentence
