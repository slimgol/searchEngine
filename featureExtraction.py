from sklearn.feature_extraction.text import CountVectorizer
from test import normalize_list_of_strings

#corpus will be a list of strings.
def bow_extractor(corpus, ngram_range=(1,1)):
	vectorizer = CountVectorizer(min_df=1,ngram_range=ngram_range)#Accept terms with a minimum frequency of 1.
	features = vectorizer.fit_transform(corpus)

	return vectorizer, features



#The following is for testing purposes only.

from sklearn.datasets import fetch_20newsgroups
from sklearn.cross_validation import train_test_split

def get_data():
	data = fetch_20newsgroups(subset='all', shuffle=True, remove=('headers','footers','quotes'))
	return data

def prepare_datasets(corpus,labels,test_data_proportion=0.3):
	train_x, test_x, train_y, test_y = train_test_split(corpus,labels,test_size=0.33,random_state=42)
	return train_x, test_x, train_y, test_y

def remove_empty_docs(corpus, labels):
	filtered_corpus = []
	filtered_labels = []
	for doc, label in zip(corpus, labels):
		if (doc.strip()):
			filtered_corpus.append(doc)
			filtered_labels.append(label)
	return filtered_corpus, filtered_labels

dataset = get_data()
corpus, labels = dataset.data, dataset.target

train_corpus, test_corpus, train_labels, test_labels = prepare_datasets(corpus, labels, test_data_proportion=0.3)

norm_train_corpus = normalize_list_of_strings(train_corpus)
norm_test_corpus = normalize_list_of_strings(test_corpus)

bow_vectorizer, bow_train_features = bow_extractor(norm_train_corpus)
bow_test_features = bow_vectorizer.transform(norm_test_corpus)


from sklearn.naive_bayes import MultinomialNB

mnb = MultinomialNB()

mnb.fit(bow_train_features,train_labels)
predictions = mnb.predict(bow_test_features)





'''


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

'''


