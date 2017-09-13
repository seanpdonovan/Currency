import urllib.request
import xml.etree.ElementTree as ET

#user_agent needed or else forbidden request error
user_agent = 'Mozilla'
url = "http://rates.fxcm.com/RatesXML"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()

root = ET.fromstring(data)

#print the names of the currencies
for child in root:
	symbol = child.get('Symbol')
	bid = child.find('Bid').text
	print(symbol, bid)
