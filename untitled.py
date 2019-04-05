'''
This program is made for python3.
This module provides an interface for:
	Extracting text from a page.
	Normalizing the extracted text.
	Create bag of words features (bow) from a pre-trained bow vectorizer.
	Classifies text (bow features) using a pre-trained classifier.
	Returns the feature associated with the input url.
'''

'''
This program is made for python3.
The purpose of this program is to take the labeled seed pages and create a classifier from them.
Approach:
	Import seed pages.
	Extract text.
	Normalize text.
	Split pages into training and testing pages.
	Train classifier.
'''

import seedPages#Seed pages that will be used to get the training and test data for the classifier.
import trainTestData #Import function to extract text from a given url, and normalize it, returning a list of pairs of the form (url, topic).
from featureExtraction import bow_extractor
import nltk
from trainTestData import extractText#Used to extract text from a given url.
from test import normalize_text#Used to normalize the extracted text.
from sklearn.naive_bayes import MultinomialNB



def train_predict_evaluate_model(classifier, train_features, train_labels, test_features, test_labels):
	#Build model.
	classifier.fit(train_features,train_labels)
	#Predict using model.
	predictions = classifier.predict(test_features)
	#Evaluate model prediction performance.
	get_metrics(true_labels=test_labels,predicted_labels=predictions)
	return predictions



#Multinomial Naive Bayes with BOW features.
mnb_bow_predictions = train_predict_evaluate_model(classifier=mnb, train_features=bow_train_features,train_labels=train_labels,test_features=bow_test_features,test_labels=test_labels)


#Create a function to train the model.
#This function must check to determine whether or not the classifier has been trained.
#If not trained then train.
#Otherwise, load model from storage.
def trainModel(classifier):
	#TODO: Test to determine whether or not the model has been trained and stored.

	#Form a normalized tagged dataset from a set of predefined, labeled urls.
	normalized_labeled_set = trainTestData.createTaggedDataSet(seedPages.ENERGY_SEED_URLS)
	
	#TODO: Split normalized_labeled_set into training and test sets.
	#normalized_labeled_train, normalized_labeled_test --> derived from normalized_labeled_set

	#Create the train corpus, and their associated labels.
	normalized_train_corpus = []
	train_labels = []
	for pair in normalized_labeled_train:
		normalized_train_corpus.append(pair[0])#Text.
		train_labels.append(pair[1])#Label

	#Create the test corpus, and their associated labels.
	normalized_test_corpus = []
	test_labels = []
	for pair in normalized_labeled_test:
		normalized_test_corpus.append(pair[0])#Text
		test_labels.append(pair[1])#Label

	#Bag-of-words features.
	#Train bow vectorizer on the normalized train corpus.
	bow_vectorizer, bow_train_features = bow_extractor(normalized_train_corpus)
	#Use the trained vectorizer to transform the normalized test corpus, to create the bag of words for the normalized test corpus.
	bow_test_features = bow_vectorizer.transform(normalized_test_corpus)

	#Build model using the bow training features, and the corresponding labels.
	classifier.fit(bow_train_features, train_labels)





#TODO: Instantiate classifier here.
mnb = MultinomialNB()

#TODO: Explain what this function does.
def makePrediction(url):
	text = extractText(url)
	if (text == None):
		return None
	#Normalize text.
	normalizedText = normalize_text(text)
	#Create bag of words features from the normalized text. We will use our pre-trained bow vectorizer.
	bow_features = bow_vectorizer.transform([normalizedText])#Note that "transform" method accepts a list of strings.
	#Make prediction.
	prediction = classifier.predict(bow_features)
	return prediction #TODO: Explain what data type is returned, and also whatelese needs to be done.
	








