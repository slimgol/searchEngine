from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin

def crawl_(seed, depth=2):
    urlQueue = list()#Set up queue.
    urlQueue.append(seed)#Enqueue seed url.

    #Perform a breadth first search to the specified depth.
    for i in range(depth):
        if (len(urlQueue) == 0):#No urls in queue.
            return#There are no urls to search.
        
        currentUrl = urlQueue.pop(0)#Get (dequeue) first url in queue.
        try:
            currentPage = urllib2.urlopen(currentUrl)#Open specified url.
        except URLError, error:
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

                urlQueue.append(newUrl)#Append the new url to the queue.
                
                print(newUrl)#Print the new url.

            
            

        
