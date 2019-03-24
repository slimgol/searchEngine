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


#lemmatized_text = lemmatize_tagged_text(tagged)#Lemmatize the tagged text.
#lemmatized_string = ' '.join(lemmatized_text)#Create string from a list of strings. 


'''This method accepts a string, and returns a string.'''
def remove_stopwords(text):
	text_list = text.split()#Split string into array of tokens.
	new_text = []
	#Create a new list without the stopwords.

	for t in text_list:
		if t not in stopwords:
			new_text.append(t)
	'''Return a string- the string will be all of the elements of the list concatenated 
		together, with a single whitespace between each element.'''
	return ' '.join(new_text)


#print(lemmatized_string)
#print(remove_stopwords(lemmatized_string))


'''Given an input string perform the following operations:
	expand contractions, 
	lemmatize text,
	remove special characters,
	remove stopwords,
	return the resultant string.'''

t = "Hey there how are you doing. aren't you haven't you've play the game a the"
#tokenized_str = ' '.join(tokenize(t))
#print(tokenized_str)
print(t)
t_ = expandContractions(t)#String.
#tokens_list = nltk.word_tokenize(t)
#print(tokens_list)
#print(tokens_list)
print(t_.split())
tagged = nltk.pos_tag(t_.split())#List of tuples.
tagged_wn = convert_to_wn(tagged)#List of tuples; wordnet form.
lemmatized_text = lemmatize_tagged_text(tagged_wn)#Is list of words.
lemmatized_str = ' '.join(lemmatized_text)#Is string of words.
lemmatized_str = remove_stopwords(lemmatized_str)#Is a string of words (does not contain stopwords).
print(lemmatized_str)
'''
def normalize_text(text):
	tokens_list = nltk.word_tokenize(tokenized_str)
	tagged = nltk.pos_tag(tokens_list)
	tagged = convert_to_wn(tagged)
	lemmatized_text = lemmatize_tagged_text(tagged)#Lemmatize the tagged text.
	lemmatized_string = ' '.join(lemmatized_text)#Create string from a list of strings. 

	#Remove special characters. 
	return lemmatized_string

normalize_text("Hey there how are you doing. aren't you have'nt you've play the game a the")
print(normalize_text("Hey there how are you doing. aren't you have'nt you've play the game a the"))
'''


