'''
This program is made for Python3.
Description: Rank a list of URLS; Return the ranked list of urls.
Approach:
	(Note that this progam needs to be modified; this approach is nowhere where optimal.)
	Accept a list of strings (These strings will have already been normalized).
	Accept a raw input search term.
	Normalize the input search term.

	what is a good algorithm for ranking the documents?
	Focus on documentation. 
'''

def sortArray(newArray):
	pass


'''
This function accepts a url, as well as the terms set as arguments and calculates the score 
of the url, using the following:
Approach:

'''

from classifier import extract_text#Used for extracting text from a given url.
from normalizer import normalize_text#Used for text normalization.

def urlScore(url, termsSet, topicWeight = 1.75):
	#Extract text from the url.
	extractedString = extract_text(url)

	if (extractedString == None):
		return None#Failed to extract text from the url.

	#Normalize the string.
	normalizedString = normalize_text(extractedString)

	#Tokenize the string.
	normalizedTokensList = normalizedString.split()

	#Calcualte term frequencies; determine the number of tokens in the text.
	termsFrequency = 0.0

	'''
	Todo: Determine whether or not the topic should be weighted heavier.
	'''
	for token in normalizedTokensList:
		if (token in termsSet):
			if (token == topic):
				termsFrequency += topicWeight
			else:
				termsFrequency += 1


	#Calculate the number of tokens per word.

	#Return the normalized score.
	pass



def rankUrls(urlList, searchTerm, topic):
	#Remove stop-words from the searchTerm.

	#Create a set from the search terms. Add the topic if it is not already included in the set. 
	#This set shall be called the terms set.

	#Create empty array to store the urls and their associated scores.
	scored_urls = []

	#Iterate over all of the urls, and calculate the scores for the urls.
	#Add the url and the score to the scored urls array.

	#Rank the scored urls and return an array containing only the ranked urls.


	






