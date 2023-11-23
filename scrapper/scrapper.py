import requests
import json
from bs4 import BeautifulSoup

# Fetch the webpage content
def	scrapper(ean, url):
	# Search for the product's ean in the url
	url = url + ean
	response = requests.get(url)
	if not response:
		return None
	soup = BeautifulSoup(response.text, "html.parser")
	if not soup:
		return None

	# Find the product URL from the search
	script_tag = soup.find_all("script", {"type": "application/ld+json"})
	arr = list(map(lambda x: json.loads(x.string), script_tag))
	url = None
	for item in arr:
		if "@type" in item.keys() and item["@type"] == 'ItemList':
			url = item["itemListElement"][0]["url"]
			break
	# Search for the product content within the url found	
	if not url:
		return None
	response = requests.get(url)
	if not response:
		return None
	soup = BeautifulSoup(response.text, "html.parser")
	script_tag = soup.find_all("script", {"type": "application/ld+json"})
	arr = list(map(lambda x: json.loads(x.string), script_tag))
	product_data = None
	for item in arr:
		if "@type" in item.keys() and item["@type"] == 'Product':
			product_data = item
			break
	if not product_data:
		return None
	product = {}
	try:
		if script_tag: # Read data into dictionary
			product["name"] = product_data["name"]
			product["description"] = product_data["description"]
			product["brand"] = product_data["brand"]["name"]
			product["price"] = product_data["offers"]["price"]
			product["currency"] = product_data["offers"]["priceCurrency"]
	except:
		return None
	# Print dictionary for debug purposes
	print(product) 
	return product

