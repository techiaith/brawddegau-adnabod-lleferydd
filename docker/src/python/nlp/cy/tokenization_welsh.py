#!/usr/bin/env python3
#coding: utf-8
import os, sys
import re
import datetime

class tokenizer(object):

    valid_letters_lower = 'aáàâäbcdeéèêëfghiíìîïjklmnoóòôöpqrstuúùûüvwẃẁŵẅxyýỳŷÿz'
    valid_letters_upper = valid_letters_lower.upper()
    valid_numbers = '0-9'

    regex_letter = r"[" + valid_letters_lower + valid_letters_upper + r"]"
    regex_number = r"[" + valid_numbers + "]"

    regex_letter_number = r"[" + valid_letters_lower + valid_letters_upper + valid_numbers + r"-_]"

    regex_number_match = re.compile(regex_number)
    regex_letter_match = re.compile(regex_letter)

    regex_not_letter = r"[^" + valid_letters_lower + valid_letters_upper + r"-_]"
    regex_not_letter_number = r"[^" + valid_letters_lower + valid_letters_upper + valid_numbers + r"-_\[\]\*\&]"

    regex_not_letter_number_match = re.compile(regex_not_letter_number)

    regex_separator = r"[\\,\.\?!()\";/\\|`]"
    regex_separator_match = re.compile(regex_separator)


    clitics = ['ch','i','m','n','r','th','u','w']
    valid_clitic_apostraphes = ["'","\u2018", "\u2019","\u02BC"]

    regex_clitics=r":|-"

    regex_single_quotes = "[\'\u2018\u2019]"
    regex_double_quotes = "[\"\u201C\u201D]"


    def __init__(self):
        #regex_clitics = r":|-|'CH|'ch|'I|'i|'M|'m|'N|'n|'R|'r|'TH|'th|'U|'u|'W|'w"
        for c in self.clitics:
            for a in self.valid_clitic_apostraphes:
                self.regex_clitics+="|%s%s|%s%s" % (a, c, a, c.upper())
        self.regex_clitics_match = re.compile(self.regex_clitics)

        
    def detokenize(self, string):
        s = string
        s = ' '.join(s)
        s = re.sub(r' (' + self.regex_clitics + ')$', r"\g<1>", s)
        s = re.sub(r' (' + self.regex_separator + ')', r"\g<1>", s)
        return s.strip()


    def tokenize(self, string):
        s = string
        s = re.sub('\t', " ", s)
        s = re.sub("(" + self.regex_separator + ")", " \g<1> ", s)
        s = re.sub("(" + self.regex_not_letter_number + ")'", "\g<1> '", s)
        s = re.sub("(" + self.regex_clitics + ")$", " \g<1>", s)
        s = re.sub("(" + self.regex_clitics + ")(" + self.regex_not_letter_number + ")", " \g<1> \g<2>", s)
        s = re.sub(self.regex_double_quotes + "(.*?)" + self.regex_double_quotes, "\" \g<1> \"", s)

        result = []
        for t in s.strip().split():
            if self.isClitic(t): 
                result.append(t)
                continue

            ot=t
            t = re.sub(self.regex_single_quotes + "(.*?)", "\' \g<1>", t)
            t = re.sub("(.*?)" + self.regex_single_quotes, "\g<1> \'", t)
            if ot!=t:
                result.extend(t.split())
            else:
                result.append(t) 

        return result
        #return s.strip().split()



    def count_word_tokens(self, string):
        tokens = self.tokenize(string)
        count=0
        for t in tokens:
            if self.isClitic(t): continue
            if self.isSeparator(t): continue
            count+=1
        return count


    def tokenize_exclude_clitics(self, string):
        s = string
        s = re.sub('\t', " ", s)
        s = re.sub("(" + self.regex_separator + ")", " \g<1> ", s)
        s = re.sub("(" + self.regex_not_letter_number + ")'", "\g<1> '", s)

        return s.strip().split()


    def sub_separators(self, string, replace):
        s = string
        s = re.sub("(" + self.regex_separator + ")", replace, s)
        return s

 
    def sub_clitic_apostraphes(self, string, replace):
        s = string
        for a in self.valid_clitic_apostraphes:
            s = s.replace(a,replace)
 
        return s


    def sub_non_letter_number(self, string, replace):
        return re.sub("(" + self.regex_not_letter_number + ")", replace, string)

 
    def isClitic(self, string):
        if (self.regex_clitics_match.match(string)):
            return True
        else:
            return False

    def isApostraphe(self, string):
        if string in self.valid_clitic_apostraphes:
            return True
        else:
            return False

    def isSeparator(self, string):
        # @todo - not quite 'is'. finds matching substring, doesn't equate the entire string
        if (self.regex_separator_match.match(string)):
            return True
        else:
            return False

    def isNotNumberOrLetter(self, string):
        if (self.regex_not_letter_number_match.match(string)):
            return True
        else:
            return False

    def containsNotLetterNumber(self, string):
        matches = self.regex_not_letter_number_match.findall(string)
        if len(matches)>0:
            return True
        else:
            return False

 
    def containsNumbers(self, string):
        numbers = self.regex_number_match.findall(string)
        if len(numbers)>0:
            return True
        return False
       
    
    def remove_seperators(self, string):
        tokens = self.tokenize(string)
        new_tokens = []
        for tok in tokens:
            s = re.sub(self.regex_separator,"", tok)
            if len(s) > 0:
                new_tokens.append(tok)

        return self.detokenize(new_tokens)


if __name__ == "__main__":

    t = tokenizer()
    #print(t.sub_separators("dwi, ddim",""))
    #print(t.sub_clitic_apostraphes("[i'r]","_"))
    print (str(t.tokenize(sys.argv[1])))

