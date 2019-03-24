import re
from CONTRACTIONS_LIST import cList#Import dictionary containing contractions, and their mapping.
import nltk#Library for natural language processing.
import string
from nltk.stem import WordNetLemmatizer#To help with lemmatizing words.

c_re = re.compile('(%s)' % '|'.join(cList.keys()))

stopwords_list = nltk.corpus.stopwords.words('english')#Create a list of all stop words.
wnl = WordNetLemmatizer()#Instantiate WordNetLemmatizer class.

''''Define a function to take care of tokenizing a given set of text. This function will 
remove any whitespaces from each of the tokens.'''

def expandContractions(text, c_re=c_re):
    def replace(match):
        return cList[match.group(0)]
    return c_re.sub(replace, text)


'''Define a function to bring words into their base form.'''

