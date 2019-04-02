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

normalized_labeled_set = trainTestData.createTaggedDataSet(seedPages.ENERGY_SEED_URLS)




'''
TODO: Prepare training and testing data sets. Thus, split the normalized labaled set into 
a normalized training set and a normalized testing set.
'''

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



############################
####FEATURE EXTRACTION######     
############################

from featureExtraction import bow_extractor
import nltk

#Bag-of-words features.
#Train bow vectorizer on the normalized train corpus.
bow_vectorizer, bow_train_features = bow_extractor(normalized_train_corpus)
#Use the trained vectorizer to transform the normalized test corpus, to create the bag of words for the normalized test corpus.
bow_test_features = bow_vectorizer.transform(normalized_test_corpus)


'''
TODO: Explain what we are doing here.
Approach:

'''

def train_predict_evaluate_model(classifier, train_features, train_labels, test_features, test_labels):
	#Build model.
	classifier.fit(train_features,train_labels)
	#Predict using model.
	predictions = classifier.predict(test_features)
	#Evaluate model prediction performance.
	get_metrics(true_labels=test_labels,predicted_labels=predictions)
	return predictions

from sklearn.naive_bayes import MultinomialNB

mnb = MultinomialNB()


'''
Now we will train, predict, and evaluate models for all the different types of features using
Multinomial Naive Bayes and Support Vector Machines.
'''

#Multinomial Naive Bayes with BOW features.
mnb_bow_predictions = train_predict_evaluate_model(classifier=mnb, train_features=bow_train_features,train_labels=train_labels,test_features=bow_test_features,test_labels=test_labels)












