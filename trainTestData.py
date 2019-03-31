'''
This program is built for python3.
This program is used to create the training and testing datasets for the 
text classifier.

Approach:

'''

'''Import all dependencies.'''
from bs4 import BeautifulSoup
from urllib import request


'''Function accepts a url, extracts text from the url, and then returns the extracted
text as a single string.'''
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









