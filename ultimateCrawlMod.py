'''
This program is built for python3.
This program provides functions for crawling and indexing the web.
The approach is as follows:
    Two threads will be executed simultaneously...

TODO: This program needs revision. Also, convert this program into a module by creating 
a function which must be invoked to start the threads, which in-turn take care of executing
each of the corresponding functions.

Optimizing Performance:
Derive a way of measuring the quality of links. 
Perhaps we can form a hybrid search- a mix between BFS and DFS... Perhaps when we come across a very high
quality link (where the quality exceeds some predefined threshold), then we start another thread of execution to run 
in parallel to perform a DFS on that quality node.

TODO:
---------------------------------------------------------------------------------------------------------------------
What about mutual exclusion (mutexes) locks on the global url queue, since it is 
being accessed by two threads. Generally, there wont be a problem, as data is being
added to the back of the queue and removed from the front, and data is being 
enqueued much faster than it is being dequeued (since it takes longer to process a 
url, rather than just visit it). However, this is a flaw, and it needs to be corrected.

In addition, due to the memory constraints of the system that the crawl is being performed on,
perhaps the thread that is taking care of the crawling should be timed out for a bit, if the 
size of the queue exceeds a certain threshold. This is so that the thread that is processing
the queue (classifying and storing in the database) can have some time to "catch-up" (by removing
some of the elements from the memory, and placing them in storage (the database)). 
Or perhaps, we can introduce a third thread that is usually asleep, and periodically "wakes-up" to
check the memory consumption, and if necessary, signals a temporary timeout for the "crawler" thread.
Note, this is all necessary because crawling can take a couple of days or even weeks, and thus, runs 
the risk of causing the program to crash, due to too much memory consumption.
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
                    ==alike_flag: if set to True, this means that there is a very similar url which has 
                    ==been visited already.
                    ==If alike_flag is set to true, then do not do any futher processing on that url; skip 
                    ==to the next iteration of the for loop. 
                    ======================================================================================='''
                    '''alike_flag = False
                    for tempUrlStr in visitedUrls:
                        if (tempUrlStr in newUrl or newUrl in tempUrlStr): 
                            alike_flag = True

                    if (alike_flag):
                        continue'''
                    #########################
                    #### NEWLY ADDED END ####  
                    #########################

                    

                    if (newUrl not in visitedUrls):
                        urlQueue.append(newUrl)#Append the new url to the queue.
                        globalUrlQueue.append(newUrl)#Append the new url to the global queue.
                        visitedUrls.add(newUrl)#Add the new url to the set of visited urls.
                    '''
                    urlQueue.append(newUrl)#Append the new url to the queue.
                    globalUrlQueue.append(newUrl)#Append the new url to the global queue.
                    visitedUrls.add(newUrl)#Add the new url to the set of visited urls.
                    '''


'''
TODO:
Set a termination condition. Perhaps the termination condition could once all 
of the crawling has been done, as well as all the urls in the url queue have been 
processed.
'''

def processUrlQueue():
    while(1):
        #TODO: Derive a means of breaking from this loop. What conditions must be met.
        if(not globalUrlQueue):#Queue is empty.
            time.sleep(1)#sleep for one second.
            continue#Skip the rest of instructions in current iteration.
        #Dequeue element from queue and process it.
        currentUrl = globalUrlQueue.pop(0)
        if (currentUrl in globalProcessedUrlSet):
            continue#url is already in database.
        
        urlClass = classifyUrl(currentUrl)#Classify the url.
        print(urlClass)
        print(currentUrl)
		#TODO: Store important information in database.


#crawl_(["https://www.youtube.com"])
#processUrlQueue()



#Create thread to crawl the web.
crawler_thread = threading.Thread(target=crawl_, args=(["https://en.wikipedia.org/wiki/Wind_power"], 4,))
#Create thread to process the url queue.
url_processor_thread = threading.Thread(target=processUrlQueue)

#Start the crawler thread.
crawler_thread.start()
#Start the url processor thread.
url_processor_thread.start()


crawler_thread.join()#Wait for thread to finish execution before executing the rest of instructions in the program.
url_processor_thread.join()#Wait for the thread to finish execution before executing the rest of instructions in the program.























