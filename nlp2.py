from pattern3.en import tag
from nltk.corpus import wordnet as wn

#Perform POS tagging.
def pos_tag_text(text):
	def penn_to_wn_tags(pos_tag):
		if pos_tag.startswith('J'):
			return wn.ADJ
		elif pos_tag.startswith('N'):
			return wn.NOUN
		elif pos_tag.startswith('V'):
			return wn.verb
		elif pos_tag.startswith('R'):
			return wn.ADV
		else:
			return None

	tagged_text = tag(text)
	tagged_lower_text = [(word.lower(), penn_to_wn_tags(pos_tag)) for word, pos_tag in tagged_text]
	return tagged_lower_text
