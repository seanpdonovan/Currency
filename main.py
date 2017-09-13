import urllib.request
import xml.etree.ElementTree as ET
import time

#user_agent needed or else forbidden request error
user_agent = 'Mozilla'
url = "http://rates.fxcm.com/RatesXML"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
data = response.read()

root = ET.fromstring(data)

#get the currency and target rate
Currency = input("Enter the currency to check: ")
TargetRate = input("Enter the target rate: ")
CurrentRate = 0

#main loop
while (CurrentRate != TargetRate):
	time.sleep(5)
	for child in root:
		symbol = child.get("Symbol")
		bid = child.find("Bid").text
		if (symbol == Currency):
			CurrentRate = bid
			print("Current rate is: " + CurrentRate)
