'''
This module is built for python3.
This module contains functions that are used for data normalization.
'''

import nltk
from nltk.corpus import state_union
from nltk.corpus import wordnet as wn
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
import re
from CONTRACTIONS_LIST import cList#Import dictionary containing contractions, and their mapping.
import string


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

stopwords = nltk.corpus.stopwords.words('english')

'''Note that the PunktSentenceTokenizer uses unsupervised learning, and thus we only
need some input text to train it. We will use the George Washington State Union Speech 
from 2002.'''
train_text = state_union.raw("2002-GWBush.txt")#Training text.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)#Instante PunkSentenceTokenizer.

#tokenized = custom_sent_tokenizer.tokenize("""Define a function to take care of tokenizing a given set of text. This function will 
#remove any whitespaces from each of the tokens""")

'''Function to tokenize a string of text. Accepts a string as an argument.'''
def tokenize(text):
	return custom_sent_tokenizer.tokenize(text)


#words = nltk.word_tokenize(tokenized[0])
#tagged = nltk.pos_tag(words)



'''Convert POS form into a form that can be handled by the WordNetLemmatizer lemmatizer.'''
def convert_to_wn(tagged_text):
	new_list = []
	for t in tagged_text:
		#t[1] contains the POS tag. t[1][0] contains the first character of the POS tag.
		temp_list = list(t)#Needed to update the tuple. Cannot simply change the contents of a tuple. 
		if t[1][0] == 'J':
			temp_list[1] = wn.ADJ

		elif t[1][0] == 'V':
			temp_list[1] = wn.VERB

		elif t[1][0] == 'N':
			temp_list[1] = wn.NOUN

		elif t[1][0] == 'R':
			temp_list[1] = wn.ADV

		else:
			temp_list[1] = None

		t = tuple(temp_list)
		new_list.append(t)
	return new_list


#tagged = convert_to_wn(tagged)

lemmatizer = WordNetLemmatizer()

'''Approach: Given a list of tuples of the form --> (token, POS Tag), the aim is to 
lemmatize (convert to its base form) the token, and then store the tokens in a new list.
Perhaps we will store the results in a single string... This is something to think about. 
In its current form, this method will return a list of words.'''
def lemmatize_tagged_text(tagged_text):#tagged_text is a list of tuples of the form (token, POS tag).
	'''Lemmatize tagged text and return a list.'''
	new_list = []#Create a new empty list. 
	for t in tagged_text:
		if (t[1] == wn.ADJ or t[1] == wn.VERB or t[1] == wn.NOUN or t[1] == wn.ADV):
			new_list.append(lemmatizer.lemmatize(t[0], pos=t[1]))
		else:
			new_list.append(t[0])#Do not lemmatize, as there is no POS tag to help with the process.

	return new_list



'''This method accepts a string, and returns a string.'''
def remove_stopwords(text):
	text_list = text.split()#Split string into array of tokens.
	new_text = []
	#Create a new list without the stopwords.
	for t in text_list:
		t = t.lower()
		if t not in stopwords:
			new_text.append(t)
	'''Return a string- the string will be all of the elements of the list concatenated 
		together, with a single whitespace between each element.'''
	return ' '.join(new_text)#Convert array of words to string of words, and return to the calling function.

regExp = r"[^a-zA-Z0-9]+"#Regular expression.

'''Accepts a string of text, removes all of the special characters and returns a new string.'''
def remove_special_chars(text):
	new_array = []
	for token in text.split():
		new_array.append(re.sub(regExp,'',token))
	return ' '.join(new_array)


'''Given an input string perform the following operations:
	expand contractions, 
	lemmatize text,
	remove special characters,
	remove stopwords,
	return the resultant string.
	'''
def normalize_text(text):
	text = expandContractions(text)#String of words.
	tagged = nltk.pos_tag(text.split())#List of tuples.
	#TODO: Tokenize words.
	tagged_wn = convert_to_wn(tagged)#List of tuples; wordnet form.
	lemmatized_text = lemmatize_tagged_text(tagged_wn)#Is list of words.
	lemmatized_str = ' '.join(lemmatized_text)#Is string of words.
	lemmatized_str = remove_special_chars(lemmatized_str)#Is string of words.
	lemmatized_str = remove_stopwords(lemmatized_str)#Is a string of words (does not contain stopwords).
	return lemmatized_str

'''Accepts a list of strings as input, and then normalizes each string, and returns 
a list of strings, where each string is normalized.'''
def normalize_list_of_strings(text_list):
	new_list = []
	for l in text_list:
		new_list.append(normalize_text(l))
	return new_list



'''TODO: THE CODE BELOW IS NECESSARY. IT NEEDS TO BE INTEGRATED WITH THE ABOVE.'''

def normalize_corpus_of_strings_wordlemmatizing(text_list):
	new_list = []
	for l in text_list:
		#new_list.append(' '.join(nltk.word_tokenize(l)))#Must join back to a string.
		new_list.append(nltk.word_tokenize(l))
	#Remove special characters.
	return new_list




