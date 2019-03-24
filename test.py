import nltk
from nltk.corpus import state_union
from nltk.corpus import wordnet as wn
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer


'''Note that the PunktSentenceTokenizer uses unsupervised learning, and thus we only
need some input text to train it. We will use the George Washington State Union Speech 
from 2002.'''
train_text = state_union.raw("2002-GWBush.txt")#Training text.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize("cars and buses, plays and played")

print(tokenized)
words = nltk.word_tokenize(tokenized[0])
print(words)
tagged = nltk.pos_tag(words)
#print(tagged[0][1].startswith('N'))

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


tagged = convert_to_wn(tagged)

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

lemmatized_text = lemmatize_tagged_text(tagged)

for word in lemmatized_text:
	print(word)







