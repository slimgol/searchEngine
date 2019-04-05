'''Import all dependencies. Explain the purpose of each library in the context of this software.'''
from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin

'''
globalUrlQueue- This is so that our "url processor" function can access the global queue 
and process it. Thus, the url processor will classify the web resource and then store it in the database.
initialProcessedUrls- This set contains the set of urls that have been queried from the database; thus, 
the urls that have been processed. It is important to have this here so that we do not crawl urls that have
already been processed.
This function will accept a list of seed pages (urls).

Note that python automatically uses pass by reference with lists.
'''
def crawl_(globalUrlQueue, initialProcessedUrls, seedList, depth=4):
    '''TO DO:We need to find a way of being able to search through the urls much faster; consider a lookup table, as these have constant search time.'''

    processedUrls = initialProcessedUrls#This is a set.
    for seed in seedList:
    	urlQueue = list()#Set up the local queue. The intention is to have an empty queue whenever we start crawling from a new seed page.
    	urlQueue.append(seed)#Enqueue seed url.
    	globalUrlQueue.append(seed)#Enqueue seed url.
    	processedUrls.add(seed)
    	#Perform a breadth first search to the specified depth.
    	for i in range(depth):
        	if (len(urlQueue) == 0):#No urls in queue.
            	return#There are no urls to search.
        
        	currentUrl = urlQueue.pop(0)#Get (dequeue) first url in queue.
        
        	try:
            	currentPage = urllib2.urlopen(currentUrl)#Open specified url.
        	except: #URLError error:
            	print(error.reason)#Print the cause of the error.
            	continue 

        	'''Create object (of the BeautifulSoup class) to parse the HTML on currentPage.'''
        	soup = BeautifulSoup(currentPage.read())

        	'''Note that all links will be contained within the "href" attribute of the "a" tag. Thus, find all instances of this tag.'''
        	adjacentLinks = soup.find_all('a')

        	'''Approach: We are viewing the web as a large directed cyclic graph, that we will be performing a breadth first search on, up to a specifed depth. Each web address is viewed as a node (of the graph), and each url on the current web address will be viewd as an adjacent node to the current node (current web address). Thus, we shall now iterate over all of the adjacent nodes, adding them to our url queue.'''

        	for link in adjacentLinks:#Iterate over all links found on the current page.
         	   '''Test to determine whether or not the current link is a real link, i.e., test if it contains the 'href' attribute.'''
            	if (link.get('href') != None):
                	newUrl = urljoin(currentUrl, link.get('href'))#Join base url (current url) with url on current page.
                	if (newUrl not in processedUrls):
                    	urlQueue.append(newUrl)#Append the new url to the queue.
                    	globalUrlQueue.append(newUrl)
                    	processedUrls.add(newUrl)


   
    
