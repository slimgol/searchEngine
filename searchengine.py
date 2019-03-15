import urllib2
from BeautifulSoup import *
from urlparse import urljoin

#Create list of words to ignore.
ignoreWords = set(['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it'])


class crawler:
    #Initialize the crawler with the name of the database.
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    #Auxiliary function for getting an entry id and adding it if it is not present.
    def getentryid(self, table, field, value, createnew=True):
        return None

    #Index an individual page.
    def addtoindex(self, url, soup):
        print('Indexing %s' % url)

    #Extract text from an HTML page (no tags).
    def gettextonly(self, soup):
        return None

    #Separate the words by any non-whitespace character.
    def separatewords(self, text):
        return None

    #Return true if this url is already indexed.
    def isindexed(self, url):
        return False

    #Add link between two pages.
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    #Starting with a list of pages, do a breadth first search to the given depth, indexing pages as we go.
    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print("Could not open %s" % page)
                    continue
                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url = urljoin(page, link['href'])
                        if url.find("'")!=-1: continue
                        url = url.split('#')[0]#Remove location portion.
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)#Add URL.
                        linkText = self.gettextonly(link)#Extract the text from the web resource.
                        self.addlinkref(page, url, linkText)

                        self.dbcommit()#Save the changes made to the database.
                pages = newpages

    #Create the database tables.
    def createindextables(self):
        pass

    
