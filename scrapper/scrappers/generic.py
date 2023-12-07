import requests
import json
from bs4 import BeautifulSoup

headers = {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'
 }


def get_page_results(url):
	response = requests.get(url, headers=headers)
	if not response:
		return None
	return BeautifulSoup(response.text, "html.parser")
	

def extract_product_url(page_results, results_classes):
	result_links = page_results.select(results_classes)
	if len(result_links) == 0:
		return None
	return result_links[0].get("href")

def	get_product_url(base_url, search_url, ean, results_classes):
	page_results = get_page_results(search_url + ean)
	if not page_results:
		return None
	product_url = extract_product_url(page_results, results_classes)
	if not product_url:
		return None
	# prepend base_url if the path is relative
	if product_url[0] == "/":
		product_url = base_url + product_url
	return product_url
	

def	scrapper(base_url, search_url, ean, results_classes):
	product_url = get_product_url(base_url, search_url, ean, results_classes)
	if not product_url:
		return None

	print(product_url)
	return None


	# Search for the product content within the url found	
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
