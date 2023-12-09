#StockPriceSearch
#importing the important modules required for execution
import re
import urllib.request
#Storing the array of stocks and the initial url
url = "https://www.google.com/search?q="
#Input of the stock required
stock = input("Enter your stock: ")
url = url + stock
#Reading the data of the stock
data= urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
#Searching for the required price data
m = re.search('idfc itemprice="89.15"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("The value of " + stock.upper() + " is " + final)