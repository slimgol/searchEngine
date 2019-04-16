'''
This program is built for python3.
This program provides functions for crawling and indexing the web.
The approach is as follows:
    Two threads will be executed simultaneously...

TODO: This program needs revision. Also, convert this program into a module by creating 
a function which must be invoked to start the threads, which in-turn take care of executing
each of the corresponding functions.
'''



from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urljoin
import time #Will be used to force thread to sleep.
import threading #Will be used to achieve parallelism.
from classifier import classifyUrl #Function to classify urls.

'''
Approach:
We will need to use a global a few global variables so that two threads can access the resources.
'''


#Query database and store all urls in a set (globalProcessedUrlSet).
#Empty set.
globalProcessedUrlSet = set()
#TODO: Query the database for all of the urls. Add each url to the set.

#Declare a gloabl url queue that is initially empty.
globalUrlQueue = list()#Create empty list.


'''
globalUrlQueue- This is so that our "url processor" function can access the global queue 
and process it. Thus, the url processor will classify the web resource and then store it in the database.
initialProcessedUrls- This set contains the set of urls that have been queried from the database; thus, 
the urls that have been processed. It is important to have this here so that we do not crawl urls that have
already been processed.
This function will accept a list of seed pages (urls).

Note that python automatically uses pass by reference with lists.
'''
def crawl_(seedList, depth=4):
    '''TO DO:We need to find a way of being able to search through the urls much faster; consider a lookup table, as these have constant search time.'''

    #Maintain a set of all the visited urls.
    visitedUrls = globalProcessedUrlSet.copy()#Copy the global set. Also note that in the end, the globalProcessedSet will be a subset of the visitedUrls set.
    	#This is due to the fact that urls must first be visited and then processed.
    for seed in seedList:
        urlQueue = list() #Set up the local queue. The intention is to have an empty queue whenever we start crawling from a new seed page.
        urlQueue.append(seed) #Enqueue seed url.
        globalUrlQueue.append(seed) #Enqueue seed url.
        visitedUrls.add(seed)  #Add seed to the set of visited urls.
    	#Perform a breadth first search to the specified depth.
        for i in range(depth):
            if(len(urlQueue)==0): #No urls in queue.
                return None #There are no urls to search.
        
            currentUrl = urlQueue.pop(0) #Get (dequeue) first url in queue.
        
            try:
                currentPage = request.urlopen(currentUrl) #Create a handle to the web resource.
            except: 
                print("Could not open page.")
                continue 

            '''Create object (of the BeautifulSoup class) to parse the HTML on currentPage.'''
            soup = BeautifulSoup(currentPage.read())

            '''Note that all links will be contained within the "href" attribute of the "a" tag. 
            Thus, find all instances of this tag.'''
            adjacentLinks = soup.find_all('a')

            '''Approach: We are viewing the web as a large directed cyclic graph, 
            that we will be performing a breadth first search on, up to a specifed depth. 
            Each web address is viewed as a node (of the graph), and each url on the current 
            web address will be viewd as an adjacent node to the current node 
            (current web address). Thus, we shall now iterate over all of the adjacent nodes,
            adding them to our url queue.'''

            for link in adjacentLinks:#Iterate over all links found on the current page.
                '''Test to determine whether or not the current link is a real link, i.e., test if it contains the 'href' attribute.'''
                
                if (link.get('href') != None):
                    newUrl = urljoin(currentUrl, link.get('href'))#Join base url (current url) with url on current page.
                    
                    #############################
                    #### NEWLY ADDED BEGIN ######
                    #############################
                    '''====================================================================================
                    ==Iterate over all of the visited urls, and determine whether or not the new url is 
                    ==either a sub-string or a super-string of any of the urls in the set of urls that have
                    ==been visited already.
                    ======================================================================================='''
                    alike_flag = False
                    for tempUrlStr in visitedUrls:
                        if (tempUrlStr in newUrl or newUrl in tempUrlStr):
                        alike_flag = True

                    if (alike_flag):
                        continue
                    #########################
                    #### NEWLY ADDED END ####  
                    #########################

                    if (newUrl not in visitedUrls):
                        urlQueue.append(newUrl)#Append the new url to the queue.
                        globalUrlQueue.append(newUrl)#Append the new url to the global queue.
                        visitedUrls.add(newUrl)#Add the new url to the set of visited urls.


'''
def processUrlQueue():
	while(1):
		#TODO: Derive a means of breaking from this loop. What conditions must be met.

		if (not globalUrlQueue):#Queue is empty.
			time.sleep(1)#sleep for one second.
			continue#Skip the rest of instructions in current iteration.
		#Dequeue element from queue and process it.
		currentUrl = globalUrlQueue.pop(0)
		if (currentUrl in globalProcessedUrlSet):
			continue#url is already in database.

		urlClass = classifyUrl(currentUrl)#Classify the url.
		
		#TODO: Store important information in database.


#Create thread to crawl the web.
crawler_thread = threading.Thread(target=crawl_, args=(seedList, depth, ))
#Create thread to process the url queue.
url_processor_thread = threading.Thread(target=processedUrlQueue)

#Start the crawler thread.
crawler_thread.start()
#Start the url processor thread.
url_processor_thread.start()


crawler_thread.join()#Wait for thread to finish execution before executing the rest of instructions in the program.
url_processor_thread.join()#Wait for the thread to finish execution before executing the rest of instructions in the program.
'''






















