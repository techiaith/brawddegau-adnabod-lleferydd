#!/usr/bin/env python3
#coding: utf-8
import os
import sys

import nltk
nltk.download('words')

import nlp.cy.preprocess_welsh
import nlp.cy.tokenization_welsh 
import nlp.cy.lexicon_welsh

tokenizer=nlp.cy.tokenization_welsh.tokenizer()
lexicon=nlp.cy.lexicon_welsh.lexicon()
lexicon_en=set(nltk.corpus.words.words())

oovfile = open("filter.oov.log", 'w', encoding='utf-8')
oovfile_lex_cy = open("filter.oov.lex.cy.log", 'w', encoding='utf-8')
rejectedfile = open("filter.rejected.log", 'w', encoding='utf-8')


for line in sys.stdin:
    count=0
    valid=True
    oov=set()

    orig_line = line
    line = nlp.cy.preprocess_welsh.clean(line)

    if tokenizer.containsNumbers(line): continue

    tokens = tokenizer.tokenize(line)
    for t in tokens:
        if tokenizer.isClitic(t): continue
        if tokenizer.isSeparator(t): continue
        if tokenizer.isApostraphe(t): continue
        if tokenizer.isNotNumberOrLetter(t): continue

        if not lexicon.contains(t):            
            valid=False
            oov.add(t)
            if t in lexicon_en or t[0].isupper():
                oovfile.write("%s\n" % t)
            else:
                oovfile_lex_cy.write("%s\n" % t)
                    
        count+=1

    if count > 14: valid=False
    
    if valid: sys.stdout.write(orig_line)
    else: rejectedfile.write(line.rstrip() + "\t" + str(tokens) + "\t" + str(oov) + '\n\n')
