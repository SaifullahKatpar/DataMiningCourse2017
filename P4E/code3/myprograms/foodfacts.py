import urllib.request, urllib.parse, urllib.error
import json

url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()

fhand = open('data.txt','w')
fhand.write(data)
js = json.loads(data)
print('Retrieved', len(data), 'characters')
print(json.dumps(js, indent=4))

