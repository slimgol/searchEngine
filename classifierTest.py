'''
This program is made for python3.
The purpose of this program is to test out multiclass classification.
Approach:
1. Test out what is presented.
2. Read documentation on the tools.
3. Iterate.
'''

from sklearn.datasets import fetch_20newsgroups
from sklearn.cross_validation import train_test_split
from normalizer import normalize_list_of_strings

def get_data():
	return fetch_20newsgroups(subset='all', shuffle=True, remove=('headers','footers','quotes'))


def prepare_datasets(corpus, labels, test_data_proportion=0.3):
	train_X, test_X, train_Y, test_Y = train_test_split(corpus,labels,test_size=0.33,random_state=42)
	return train_X,test_X,train_Y,test_Y


def remove_empty_docs(corpus, labels):
	filtered_corpus = []
	filtered_labels = []
	for doc, label in zip(corpus, labels):
		if doc.strip():
			filtered_corpus.append(doc)
			filtered_labels.append(label)

	return filtered_corpus, filtered_labels


#Get the data.
dataset = get_data()

corpus, labels = dataset.data, dataset.target 
corpus, labels = remove_empty_docs(corpus, labels)

#print('Label: '+str(labels[10]))
#print('Data: '+str(dataset.target_names[labels[10]]))


train_corpus,test_corpus,train_labels,test_labels = prepare_datasets(corpus,labels)
print(train_corpus[1])

normalized_train_corpus = normalize_list_of_strings(train_corpus)#Normalize corpus of training data.
normalized_test_corpus = normalize_list_of_strings(test_corpus)#Normalize corpus of test data.
print("--------------------\n\n\n\n")
print(normalized_train_corpus[1])



'''
Everything works perfectly up to here...
Adding new code below...
'''

from featureExtraction import bow_extractor
import nltk

#Bag-of-words features.
#Train bow vectorizer on the normalized train corpus.
bow_vectorizer, bow_train_features = bow_extractor(normalized_train_corpus)
#Use the trained vectorizer to transform the normalized test corpus, to create the bag of words for the normalized test corpus.
bow_test_features = bow_vectorizer.transform(normalized_test_corpus)


#Tokenize documents.
tokenized_train = [nltk.word_tokenize(text) for text in normalized_train_corpus]


'''
Once we have extracted all of the features above, we will now define a function that will
be useful for evaluation of our classification model, based on a predefined set of metrics.
'''

from sklearn import metrics
import numpy as np

def get_metrics(true_labels, predicted_labels):
	print('Accuracy: '+str(np.round(metrics.accuracy_score(true_labels,predicted_labels),2)))
	print('Precision: '+str(np.round(metrics.precision_score(true_labels,predicted_labels,average='weighted'),2)))
	print('Recall: '+str(np.round(metrics.recall_score(true_labels,predicted_labels,average='weighted'),2)))
	print('F1 Score: '+str(np.round(metrics.f1_score(true_labels,predicted_labels,average='weighted'),2)))



'''
We will now define a function that trains the model using an ML algorithm and the training data, 
performs predictions on the test data using the trained model, and then evaluates the predictions 
using the preceeding function to give us the model performance.
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
from sklearn.linear_model import SGDClassifier

mnb = MultinomialNB()
svm = SGDClassifier(loss='hinge',n_iter=100)


'''
Now we will train, predict, and evaluate models for all the different types of features using
Multinomial Naive Bayes and Support Vector Machines.
'''

#Multinomial Naive Bayes with BOW features.
mnb_bow_predictions = train_predict_evaluate_model(classifier=mnb, train_features=bow_train_features,train_labels=train_labels,test_features=bow_test_features,test_labels=test_labels)
















