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
from test import normalize_list_of_strings

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
print("--------------------\n\n\n\n")
print(normalized_train_corpus[1])








