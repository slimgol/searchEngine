#Crawl the web continuously.

#Before any crawling begins, query the database for all the urls that pages that have been indexed.
#Store in a global queue.

#Import classifier. 
#Check to see if classifier has been trained; if not then train, otherwise, classifier is ready to be used.

#Note that the classifier will not be used immediately. 


#Each crawler will crawl a list of seed pages in its specific domain.
#Check the global queue to makesure that a particular url has not been indexed before storing that 
#url in the queue.

#The sixth thread will take care of repeatedly iterating over the queue and then classifying 
#each url and then storing that url to the database.
#If the queue is empty then set a timeout for this thread for a few seconds. 


from modifiedCrawler import crawl_
import time #Will be used to force thread to sleep.


#Query database and store all urls in a set (globalProcessedUrlSet).

#Declare a gloabl url queue that is initially empty.
#This queue will be used for processing all of the urls.

def processUrlQueue(urlQueue):
	while(1):
		#TODO: Derive a means of breaking from this loop. What conditions must be met.
		if (not urlQueue):#Queue is empty.
			time.sleep(1)#sleep for one second.
			continue#Skip the rest of instructions in current iteration.
		#Dequeue element from queue and process it.
		currentUrl = urlQueue.pop(0)#Get first element in queue.
		if (currentUrl in globalProcessedUrlSet):
			continue#url is already in database.
		#TODO: Classify web resource.
		#TODO: Store important information in database.





















