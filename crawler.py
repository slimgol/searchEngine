'''Import all dependencies. Explain the purpose of each library in the context of this software.'''
from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin

def crawl_(seed, depth=4):
    '''TO DO:We need to find a way of being able to search through the urls much faster; consider a lookup table, as these have constant search time.'''

    processedUrls = set()#Set to stored the processed urls.
    
    urlQueue = list()#Set up queue.
    urlQueue.append(seed)#Enqueue seed url.
    processedUrls.add(seed)
    #Perform a breadth first search to the specified depth.
    for i in range(depth):
        if (len(urlQueue) == 0):#No urls in queue.
            return#There are no urls to search.
        
        currentUrl = urlQueue.pop(0)#Get (dequeue) first url in queue.
        #processedUrls.add(currentUrl)#Add current url to the set.
        
        try:
            currentPage = urllib2.urlopen(currentUrl)#Open specified url.
        except: #URLError error:
            print(error.reason)#Print the cause of the error.
            continue 

        '''Create object (of the BeautifulSoup class) to parse the HTML on currentPage.'''
        soup = BeautifulSoup(currentPage.read())

        #TODO: Add to index.

        '''Note that all links will be contained within the "href" attribute of the "a" tag. Thus, find all instances of this tag.'''
        adjacentLinks = soup.find_all('a')

        '''Approach: We are viewing the web as a large directed cyclic graph, that we will be performing a breadth first search on, up to a specifed depth. Each web address is viewed as a node (of the graph), and each url on the current web address will be viewd as an adjacent node to the current node (current web address). Thus, we shall now iterate over all of the adjacent nodes, adding them to our url queue.'''

        for link in adjacentLinks:#Iterate over all links found on the current page.
            '''Test to determine whether or not the current link is a real link, i.e., test if it contains the 'href' attribute.'''
            if (link.get('href') != None):
                newUrl = urljoin(currentUrl, link.get('href'))#Join base url (current url) with url on current page.
                #TODO: Do some more processing here.
                if (newUrl not in processedUrls):
                    urlQueue.append(newUrl)#Append the new url to the queue.
                    processedUrls.add(newUrl)
                #print(newUrl)#Print the new url.

    for item in processedUrls:
        print(item)
    '''This si just some information that will help us during the development phase. The queue should have 'depth' less elements than the set of processed urls. Explain why this is.'''
    print(len(processedUrls))
    print(len(urlQueue))
    

            
            

        
