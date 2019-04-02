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

print(normalized_labeled_set[0])