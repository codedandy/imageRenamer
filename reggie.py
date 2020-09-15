import re

exReggie = r'[\.jpg|\.png|\.gif]'
imgRegex = re.compile(r'<img.+?src=\".*?/?(.+?{})\".+?/>'.format(exReggie))
nestedImg = re.compile(r'^(.*?)/([a-zA-Z0-9\-_\.%]*?{})$'.format(exReggie))

def removeFilePath(imageList):
    returnList = []

    for each in imageList:
	    if "/" in each:
	    	finder = nestedImg.search(each)
	    	found = finder.group(2)
	    	returnList.append(found)
	    else:
	    	returnList.append(each)
    
    return returnList


# testList = ["img/20.09.14%201985%20H%E2%80%93M_html_290f13663053bc67.jpg"]
# print(removeFilePath(testList))

# nonSet = ["list", "list", "tingle"]
# isSet = list(set(nonSet))
# print(isSet)
