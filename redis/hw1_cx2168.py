import urllib
from ast import literal_eval
contents = urllib.urlopen('https://api.nasa.gov/planetary/apod?api_key=lCQW04CcqbqQxjxZMIzGqinNRKWH5Iw9GKM4uSkc&date=2017-09-02').read()
print(literal_eval(contents)['url'])
