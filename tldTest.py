from urllib.parse import urlparse

#Uses urlib to return network location (web.site.TopDomain)
def getSubDomain(url):
	try:
		return urlparse(url).netloc
	except:
		return 'de' 

# Splits the url name and returns the top and second level domain (Site.com)
def getDomain(url):
	try:
		results = getSubDomain(url).split('.')
		return results[-2] + '.' + results[-1]
	except: 
		return 'u '
	
#Returns top level domain (com,gov,org)
def getTopLevelDomain(url):
	try:
		results = getSubDomain(url).split('.')
		return results[-1]
	except:
		return 'sdc'


print(getSubDomain('https://www.youtube.com/watch?v=PPonGS2RZNc&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&index=14'))
print(getDomain('https://www.youtube.com/watch?v=PPonGS2RZNc&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&index=14'))
print(getTopLevelDomain('https://www.youtube.com/watch?v=PPonGS2RZNc&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q&index=14'))
