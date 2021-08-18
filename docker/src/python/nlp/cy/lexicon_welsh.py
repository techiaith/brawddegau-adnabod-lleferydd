import os
import wget

from os import listdir
from zipfile import ZipFile
from collections import defaultdict

import nlp.cy.trie

LEXICON_URL='https://raw.githubusercontent.com/techiaith/lecsicon-cymraeg-bangor/main/lecsicon_cc0.zip'
LEXICON_FILENAME='lecsicon_cc0.txt'

clitics = ['CH','I','M','N','R','TH','U','W']
#missing_valid_wordforms = ['fod','gael','wneud','ddod','fynd','enwau','awyrennau','ffrindiau',
#        'mynyddoedd',]

class lexicon(object):

    def __init__(self):

        self.lex_trie = nlp.cy.trie.Trie()
        for c in clitics: self.lex_trie.insert(c.upper())
        #for m in missing_valid_wordforms: self.lex_trie.insert(m.upper())
        self.wordform_lookup = defaultdict(list)
        self.lemma_lookup = defaultdict(list)

        for w,l,p,f in self.read_lexicon_file():
            self.add(w,l,p,f)

        self.add('mae hen wlad fy nhadau', 'mae hen gwlad fy tadau', 'PHRASE', '')


    def read_lexicon_file(self):

        def download_lexicon():
            wget.download(LEXICON_URL)

            if os.path.isfile('lecsicon_cc0.zip'):
                z=ZipFile('lecsicon_cc0.zip','r')
                z.extractall()
                z.close()

            for fn in os.listdir():
                if fn.endswith('.zip') or fn.endswith('.tmp'):
                    os.remove(fn)

            #print ("\n")

        def parse_entry(lex_entry):
            def parse_ud_fields(ud_string):
                p=dict()
                ud = ud_string.split('|')
                for m in ud:
                    f = m.split('=')
                    p[f[0]]=f[1]
                return p

            f = lex_entry.rstrip().split('\t')
            return f[0], f[1], f[2], parse_ud_fields(f[3]) if len(f)>3 else ''

        if not os.path.isfile(LEXICON_FILENAME):
            #print ("Llwytho'r lecsicon i lawr..")
            download_lexicon()

        #print ("Llwytho'r geirfa...") 
        with open(LEXICON_FILENAME, 'r', encoding='utf-8') as lexicon_file:
            for lex in lexicon_file:
                wordform, lemma, pos, ud = parse_entry(lex)
                yield (wordform, lemma, pos, ud)

        oov_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "oov_welsh.txt")
        with open(oov_file_path, 'r', encoding='utf-8') as oov_file:
            for oov_entry in oov_file:
                wordform=oov_entry.lstrip().split(" ", 1)[1]
                yield (wordform,'','','')



    def contains(self, word):
        return self.lex_trie.search(word.upper())

    def get_lemmas_with_info(self, wordform):
        return '\n'.join('{}\tLemma:{}\tPos:{}\tInfo:{}'.format(query, *l) for l in self.get_lemmas(query))

    def get_lemmas(self, wordform):
        return self.wordform_lookup[wordform]

    def get_wordforms(self, lemma):
        return self, lemma_lookup[lemma]

    def add(self, wordform, lemma, pos, features):
        self.lex_trie.insert(wordform.upper())
        self.wordform_lookup[wordform].append((lemma,pos,features))
        self.lemma_lookup[lemma].append((wordform,pos,features))

    def get_size(self):
        return len(self.wordform_lookup), len(self.lemma_lookup)


if __name__ == "__main__":
    l=lexicon() 
    print (l.get_size())
    print ("Lecsicon wedi'i llwytho")

