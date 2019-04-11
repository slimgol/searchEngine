from sklearn.feature_extraction.text import CountVectorizer

#corpus will be a list of strings.
def bow_extractor(corpus, ngram_range=(1,1)):
	vectorizer = CountVectorizer(min_df=1,ngram_range=ngram_range)#Accept terms with a minimum frequency of 1.
	features = vectorizer.fit_transform(corpus)

	return vectorizer, features



#The following is for testing purposes only.

CORPUS = [
"good day sir how are you today", 
"today is a lovely day for training",
"today the sun is lovely what a day for track n field training"
]
bow_vectorizer, bow_features = bow_extractor(CORPUS)

features = bow_features.todense()
print(features)

#Accepts a list of strings.
new_features = bow_vectorizer.transform(["Hello sir how are you what a day for training"])
new_features = new_features.todense()
print(new_features)


