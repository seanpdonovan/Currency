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

#array of available currency symbols
availableCurrencies = []
for child in root:
	symbol = child.get("Symbol").upper()
	availableCurrencies.append(symbol)
	
#get the currency and target rate
Currency = input("Enter the currency to check: ").upper()
if ((Currency not in availableCurrencies)):
	print("This currency is not available")
	Currency = input("Enter the currency to check: ").upper()
TargetRate = input("Enter the target rate: ")
if (TargetRate == None):
	TargetRate = input("Enter the target rate: ")
CurrentRate = None

def getCurrentRate():
	for child in root:
		symbol = child.get("Symbol")
		bid = child.find("Bid").text
		if (symbol == Currency):
			return bid

CurrentRate = getCurrentRate()

def isLower(current, target):
	return current < target

initiallyLower = isLower(CurrentRate, TargetRate)
currentlyLower = initiallyLower

#main loop
while (CurrentRate != TargetRate and initiallyLower == currentlyLower):
	time.sleep(5)
	CurrentRate = getCurrentRate()
	print("Current rate is: " + CurrentRate)
	currentlyLower = isLower(CurrentRate, TargetRate)
