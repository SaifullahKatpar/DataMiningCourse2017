import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('https://www.enterprise.co.uk/content/dam/global-vehicle-images/cars/VAUX_INSI_2014.png').read()
fhand = open('car.jpg', 'wb')
fhand.write(img)
fhand.close()
