import re
from CONTRACTIONS_LIST import cList#Import dictionary containing contractions, and their mapping.
import nltk#Library for natural language processing.
import string
from nltk.stem import WordNetLemmatizer#To help with lemmatizing words.

c_re = re.compile('(%s)' % '|'.join(cList.keys()))

def expandContractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)


