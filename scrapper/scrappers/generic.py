import requests
import json
from bs4 import BeautifulSoup

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
 }


def get_page_results(ean, url):
	response = requests.get(url + ean, headers=headers)
	if not response:
		return None
	return BeautifulSoup(response.text, "html.parser")
	

def get_product_url(page_results):
	search_links = page_results.select()
	if len(search_links) == 0:
		return None
	return search_links[0].get("href")
	

def	scrapper(ean, url, search_classes):
	# Search for the product's ean in the url
	page_results = get_page_results(ean, url)
	if not page_results:
		print("No page results")
		return None
	
	print(page_results)
	return None
	
	product_url = get_product_url(page_results, search_classes)
	if not product_url:
		print("No product url found")
		return None
	

	# Find the product URL from the search
	script_tag = soup.find_all("script", {"type": "application/ld+json"})
	arr = list(map(lambda x: json.loads(x.string), script_tag))
	url = None
	for item in arr:
		if "@type" in item.keys() and item["@type"] == 'ItemList':
			if not len(item["itemListElement"]):
				return None
			url = item["itemListElement"][0]["url"]
			break

	# Search for the product content within the url found	
	if not url:
		return None
	response = requests.get(url, headers=headers)
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
		product["name"] = product_data["name"]
		product["description"] = product_data["description"]
		product["brand"] = product_data["brand"]["name"]
		product["price"] = product_data["offers"]["price"]
		product["currency"] = product_data["offers"]["priceCurrency"]
		product["url"] = url
	except:
		return None
	return product



scrapper("5601012011500", "https://www.continente.pt/pesquisa/?q=", ".results-section .product a")