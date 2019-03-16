from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin

def crawl_(seed, depth=2):
    urlQueue = list()#Set up queue.
    urlQueue.append(seed)#Enqueue seed url.

    #Perform a breadth first search to the specified depth.
    for i in range(depth):
        #TODO: Check to makesure that the queue is not empty.
        currentUrl = urlQueue.pop(0)#Get first url in queue.
        try:
            currentPage = urllib2.urlopen(currentUrl)#Open specified url.
        except URLError, error:
            print(error.reason)#Print the cause of the error.
            continue'''Ignore the rest of instructions in this current iteration, and proceed to the next iteration.'''

        
