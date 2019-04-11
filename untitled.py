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
import nltk
from trainTestData import extractText#Used to extract text from a given url.
from test import normalize_text#Used to normalize the extracted text.
from sklearn.naive_bayes import MultinomialNB
import random#Used for generating pseudorandom numbers.
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup
from urllib import request
from test import normalize_text#Import function to normalize a string of text.



'''
This function will accept a list of strings and train a bag-of-words (bow) feature extractor.
This function returns the trained bow feature extractor, as well as the corresponding features that
were produced from the list of strings. Thus, it will return a list of lists (engineered features).
'''
def bow_extractor(corpus, ngram_range=(1,1)):
	vectorizer = CountVectorizer(min_df=1,ngram_range=ngram_range)#Accept terms with a minimum frequency of 1.
	features = vectorizer.fit_transform(corpus)

	return vectorizer, features




'''
Function accepts a url, extracts text from the url, and then returns the extracted
text as a single string.
'''

def extractText(urlString):
	try:
		page = request.urlopen(urlString)
	except:
		print("Could not open page")
		return None

	soup = BeautifulSoup(page.read())

	'''Extract all meaningful data. Note that we want any data that will be useful
	in training a text classigier. Thus, paragraphs, headers, etc...'''

	paragraphList = soup.find_all('p')
	paragraphString = ""#Create an empty string.
	for paragraph in paragraphList:#Iterate over all paragraphs.
		paragraphString = paragraphString + " " + paragraph.get_text()

	return paragraphString





'''This accepts a list of pairs--> (url, topic),
and returns a list of pairs--> (text as single string from url, topic) 
Note that this function also normalizes the string.
Returns a list of pairs-->(normalized string, topic).'''

def createTaggedDataSet(urlTaggedList):
	taggedDataList = []#(text as single string from url, topic)
	for pair in urlTaggedList:
		text = extractText(pair[0])#Extract text from url.
		if (text != None):
			taggedDataList.append((normalize_text(text), pair[1]))#Add pair (text, topic) to list.

	return taggedDataList




'''
#TODO: This function needs some revision. Is it even necessary?
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
'''



'''
This function accepts a list of pairs of the form, (url, topic), as well as a training proportion.
The training proportion is used to indicate how much of the input training data is used for 
training and how much is used for testing. This function then returns two lists. The first list
contains the training pairs, and the second list contains the testing pairs; both of the form
(url, topic).
'''

def trainTestSplit(inputList, train_proportion=0.8):
	if (training_proportion > 1 || training_proportion < 0):
		return None

	LIST_LEN = len(inputList)#Length of the input list.
	training_indices = set()#Maintain a set of the training indexes.
	#Create lists to store the training instances and testing instances.
	training_list = []
	testing_list = []


	for i in range(int(LIST_LEN*train_proportion)):
		#Repeat until index has not been chosen.
		while (1):
			randIndex = random.randint(0,LIST_LEN-1)#Generate random integer between 0 and list length -1. (Note that if k is the length of the list then index k is not a valid index.)
			if (randIndex not in training_indices):
				break#We have found an index that has not yet been used.
		#Add index to the set of training indices.
		training_indices.add(randIndex)
		#Append element to training list.
		training_list.append(inputList[randIndex])
	for i in range(LIST_LEN):
		if (i not in training_indices):
			testing_list.append(inputList[randIndex])

	#Return the training and testing lists.
	return training_list, testing_list



'''
This function does not accept any arguments. This function checks to determine if a model has been 
trained and stored on the computer disk, if so, the function will load that model from the disk 
and return it to the calling function, otherwise it will instantiate the model, train it, and then
return it to the calling function.
'''

def trainModel():
	#TODO: Test to determine whether or not the model has been trained and stored.
	#If model is trained already, then load it from storage and return it to the calling function.

	#Instantiate the Multinomial Naive Bayes classifier.
	classifier = MultinomialNB()

	#TODO: The following name is deceiving as it is a list and not a set; change it.
	#Form a normalized tagged dataset from a set of predefined, labeled urls.
	normalized_labeled_set = createTaggedDataSet(seedPages.ENERGY_SEED_URLS)
	
	#TODO: Split normalized_labeled_set into training and test sets.
	#normalized_labeled_train, normalized_labeled_test --> derived from normalized_labeled_set
	normalized_labeled_train, normalized_labeled_test = trainTestSplit(normalized_labeled_set)

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

	#Return the trained classifier.
	return classifier


#Get trained classifier.
classifier = trainModel()



'''
This function accepts a raw url, reads the content of the web-page from the url, normalizes the
text, and uses the trained classifier to make a prediction.
This function then returns the prediction to the calling function.
'''

def classifyUrl(url):
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









