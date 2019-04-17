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


TODO:
Use a different sorting algorithm here; perhaps have different sorting algorithms.
The aim is to reduce computational cost. Thus, have two different sorting algorithms- 
one that performs well on small datasets, and another that performs well on large datasets.
Note that we must define what "small" and "large" are.
Thus, we shall sort with the algorithm that will reduce the overall computational cost.
'''
#Sort a list of pairs (url, score).
def sortArrayDescending(newArray):
	SIZE = len(newArray)

	for i in range(newArray):
		for j in range(newArray-i-1):
			if (newArray[j][1]<newArray[j+1][1]):
				#Swap elements
				temp = newArray[j]
				newArray[j] = newArray[j+1]
				newArray[j+1] = temp

	#Create a new array, containing only the urls in their ranked order.
	url_array = []

	for pair_ in newArray:
		url_array.append(pair_[0])

	return url_array


'''
This function accepts a url, as well as the terms set as arguments and calculates the score 
of the url, using the following:
Approach:

'''

from classifier import extractText#Used for extracting text from a given url.
from normalizer import normalize_text#Used for text normalization.

#TODO: Fix the weighting scheme.
def urlScore(url, termsSet, topicWeight=1):
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
	numTokens = 0#Used to store the number of tokens.

	'''
	Todo: Determine whether or not the topic should be weighted heavier.
	'''
	for token in normalizedTokensList:
		numTokens += 1
		if (token in termsSet):
			if (token == topic):
				termsFrequency += topicWeight
			else:
				termsFrequency += 1

	#Note: The following condition should not occur.
	if (numTokens == 0):
		return None 

	#Return the score.
	return termsFrequency/numTokens



def rankUrls(urlList, searchTerm, topic):
	#Normalize the raw input search term.
	normalizedSearchTerm = normalize_text(searchTerm)

	#Create array of tokens from the normalized search term.
	normalizedSearchTokens = normalizedSearchTerm.split()

	#TODO:
	#Ensure that all of the search tokens are converted to lower case.
	if (topic not in normalizedSearchTokens):
		normalizedSearchTokens.append(topic)#Add the topic to the list of search terms.

	#Create empty array to store the urls and their associated scores.
	scored_urls = []

	#Iterate over all of the urls, and calculate the scores for the urls.
	#Add the url and the score to the scored urls array.

	'''
	Iterate over all of the urls, calculate their scores, and then add them to the scored url array.
	'''
	for url in urlList:
		score = urlScore(url, normalizedSearchTokens)
		if (score == None):
			continue#Skip the rest of instructions in the current iteration.

		scored_urls.append((url, score))


	#Rank the scored urls and return an array containing only the ranked urls.
	'''
	sortArrayDescending will accept a list of tuples of the form, (url, score), and return 
	the sorted list of urls, without the score. Hence, the function will just return the 
	sorted list of urls.
	'''
	sortedUrls = sortArrayDescending(scored_urls)

	






