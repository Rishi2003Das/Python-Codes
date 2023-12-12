import requests
from bs4 import *
#https://www.accuweather.com/en/in/kolkata/206690/weather-forecast/206690
data= requests.get("https://www.accuweather.com/en/in/kolkata/206690/weather-forecast/206690")
soup=BeautifulSoup(data.text,"html.parser")
print(soup.find('div',{'class':'info'}))
data2=soup.find('div',{'class':'info'})
data3=data2.find('div',{'class':'info'})
print(data3.contents[0])