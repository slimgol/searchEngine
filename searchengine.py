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
        pass

    #Create the database tables.
    def createindextables(self):
        pass

    
