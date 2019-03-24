#import CONTRACTIONS_SET
import re#Dependency for dealing with regular expressions.
import nltk#Library for natural language processing.
import string
from nltk.stem import WordNetLemmatizer#To help with lemmatizing words.

stopwords_list = nltk.corpus.stopwords.words('english')#Create a list of all stop words.
wnl = WordNetLemmatizer()#Instantiate WordNetLemmatizer class.

'''Define a function to take care of tokenizing a given set of text. This function will 
remove any whitespaces from each of the tokens.'''

def expand_contractions(text, contraction_mapping):
	contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), flags=re.IGNORECASE|re.DOTALL)

	def expand_match(contraction):
		match = contraction.group(0)
		if (contraction_mapping.get(match)):
			expanded_contraction = contraction_mapping.get(match)
		else:
			expanded_contraction = contraction_mapping.get(match.lower())
		expanded_contraction = match[0] + expanded_contraction[1:]
		return expanded_contraction


