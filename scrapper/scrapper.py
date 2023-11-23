import requests
import json
from bs4 import BeautifulSoup

# Fetch the webpage content
def	scrapper(ean, url):
	# Search for the product
	url = url + ean
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	# Find the product URL from the search
	script_tag = soup.find("script", {"type": "application/ld+json"})
	item_list_data = json.loads(script_tag.string)
	url = item_list_data["itemListElement"][0]["url"]
	print(item_list_data)
	print();

	# Search for the product content within the url found	
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	script_tag = soup.find("script", {"type": "application/ld+json"})
	print(script_tag)	

	product = {}
	if script_tag: # Read data into dictionary
		product_data = json.loads(script_tag.string)
		product["name"] = product_data["name"]
		product["description"] = product_data["description"]
		product["brand"] = product_data["brand"]["name"]
		product["price"] = product_data["offers"]["price"]
		product["currency"] = product_data["offers"]["priceCurrency"]
	
	# Print dictionary for debug purposes
	print(product) 
	return product

