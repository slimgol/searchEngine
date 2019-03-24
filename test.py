import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer

'''Note that the PunktSentenceTokenizer uses unsupervised learning, and thus we only
need some input text to train it. We will use the George Washington State Union Speech 
from 2002.'''
train_text = state_union.raw("2002-GWBush.txt")#Training text.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize("Hello you, my name is june, and we all played in the snow.")

print(tokenized)
words = nltk.word_tokenize(tokenized[0])
print(words)
tagged = nltk.pos_tag(words)
print(tagged[0][1].startswith('N'))

def convert_to_wn(tagged_text):
	for t in tagged_text:
		


lemmatizer = WordNetLemmatizer()#Instantiate WordNetLemmatizer class.
'''
for t in tagged:
	try:
		print(lemmatizer.lemmatize(t[0], t[1]))
	except Exception as e:
		pass
'''
