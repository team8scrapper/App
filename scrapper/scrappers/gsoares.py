import requests
import json
from bs4 import BeautifulSoup

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
 }

def	scrapper(ean, url):
	# Search for the product's ean in the url
	url = url + ean
	response = requests.get(url, headers=headers)
	if not response:
		return None
	soup = BeautifulSoup(response.text, "html.parser")
	if not soup:
		return None

	soup = soup.find("script")
	url = None
	if soup:
		url = soup.string.split("\'")[1]
	# Search for the product content within the url found	
	if not url:
		return None
	response = requests.get(url, headers=headers)
	if not response:
		return None

	product = {}
	soup = BeautifulSoup(response.text, "html.parser")
	try:
		product["name"] = soup.find("meta", {"property": "og:title"}).get("content")
		product["description"] = soup.find("meta", {"property": "og:description"}).get("content")
		product["brand"] = soup.find("meta", {"itemprop": "brand"}).get("content")
		product["price"] = soup.find("meta", {"itemprop": "price"}).get("content")
		product["currency"] = soup.find("meta", {"itemprop": "priceCurrency"}).get("content")
	except:
		return None
	return product
