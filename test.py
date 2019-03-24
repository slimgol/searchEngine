import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize("Hello you, my name is june, and we all played in the snow.")

print(tokenized)
words = nltk.word_tokenize(tokenized[0])
print(words)
tagged = nltk.pos_tag(words)
print(tagged)

