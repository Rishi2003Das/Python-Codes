#Defination fetching from the web
import re
import urllib.request
try:
url = "http://dictionary.reference.com/browse/"
word = input("Enter your word: ")
url = url + word
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('meta name="description" content="', data1)
start = m.end()
end = start + 300
newString = data1[start: end]
m = re.search("See more.", newString)
end = m.start() - 1
definition = newString[0:end]
print(definition)
except:
print("I'm sorry, you're word is not in the dictionary.")