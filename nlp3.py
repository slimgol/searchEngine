from nltk.corpus import brown
from nltk.tag import RegexpTagger
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer#To help with lemmatizing words.

'''
The purpose of this code is to create a POS tagger. We will do that by creating a list of (pattern, tag) pairs.
We will then pass this list to the RegexpTagger constructor which will create a regular expression tagger,
and return the regular expression tagger object to us.
'''
wnl = WordNetLemmatizer()#Instantiate WordNetLemmatizer class.

test_sent = brown.sents(categories='news')[0]

#Create an array of (pattern, POS tag) pairs/tuples to the RegexpTagger constructor and return a Regular Expression
#Tagger object. We will then use this object to tag tokens of our text.
regexp_tagger = RegexpTagger(
     [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),   # cardinal numbers
      (r'(The|the|A|a|An|an)$', 'AT'),   # articles
      (r'.*able$', 'JJ'),				 # adjectives
      (r'.*ness$', 'NN'),                # nouns formed from adjectives
      (r'.*ly$', 'RB'),                  # adverbs
      (r'.*s$', 'NNS'),                  # plural nouns
      (r'.*ing$', 'VBG'),                # gerunds
      (r'.*ed$', 'VBD'),                 # past tense verbs
      (r'.*', 'NN')                      # nouns (default)
 ])

#Use the Regular Expression Tagger to tag our tokens.
print(regexp_tagger.tag("They have some people sampling hearded playing"))
def lemmatize_text(text):
	pos_tagged_text = regexp_tagger.tag(text)
	lemmatized_tokens = [wnl.lemmatize(word,pos_tag) if pos_tag and word!=' ' else word for word, pos_tag in pos_tagged_text]
	lemmatized_text = ''.join(lemmatized_tokens)
	return lemmatized_text








