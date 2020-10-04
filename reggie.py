import re

exReggie = r'[\.jpg|\.png|\.gif]'
imgRegex = re.compile(r'<img.+?src=\".*?/?(.+?{})\".+?/?>'.format(exReggie))
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
