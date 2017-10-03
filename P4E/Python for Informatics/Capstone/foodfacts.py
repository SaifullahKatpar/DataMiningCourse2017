import urllib.request, urllib.parse, urllib.error
import json

url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
try:
    info = json.loads(data)
except:
    info = None

product = info["product"]
countLevel =[]

def findDict(foodDict,level):
	level = level+1
	countLevel.append(level)
	if type(foodDict)==dict:
		for key in foodDict.keys():
			#print(key)
			findDict(foodDict[key],level)
findDict(info["product"],0)
print(max(countLevel))


