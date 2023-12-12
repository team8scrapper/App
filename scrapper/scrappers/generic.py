import requests
import json
from bs4 import BeautifulSoup
from babel.numbers import parse_decimal
import urllib.parse

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


def	get_product_url(store, ean):
	page_results = get_page_results(store['search_url'] + ean)
	if not page_results:
		return None
	product_url = extract_product_url(page_results, store['results_classes'])
	if not product_url:
		return None
	product_url = urllib.parse.unquote(product_url)

	# prepend base_url if the path is relative
	if product_url[0] == "/":
		product_url = store['base_url'] + product_url
	return product_url


def get_product_content(product_url):
	response = requests.get(product_url, headers=headers)
	if not response:
		return None
	return BeautifulSoup(response.text, "html.parser")
	

def	get_product_details(store, product_content, product_url):
	product = {}
	try:
		# extract data
		product["name"] = product_content.select(store['name_classes'])[0].text
		product["price"] = product_content.select(store['price_classes'])[0]
		product["price"] = product["price"].find(text=True, recursive=False)
		product["url"] = product_url
		product["currency"] = store['currency']

		# cleanup data
		product["name"] = product["name"].strip("\n");
		product["price"] = product["price"].strip("\t\n €$R");
		product["price"] = float(parse_decimal(product["price"], locale='pt_PT'))
		return product
	except:
		return None


def	scrapper(store, ean):
	product_url = get_product_url(store, ean)

	if not product_url:
		# print("no product")
		return None
	
	# print(product_url)
	product_content = get_product_content(product_url)
	if not product_content:
		return None
	# print(product_content)
	product = get_product_details(store, product_content, product_url)	
	# print(product)
	return product


# store = {
#     'search_url': "https://drive.carrefour.be/fr/search?text=",
#     'base_url': "https://drive.carrefour.be",
#     'results_classes': ".product__grid .product-item a",
#     'name_classes': ".product-details .prod-title",
#     'price_classes': ".product-details .prod-price .showRed :nth-child(2)",
# }

# print(scrapper(store, "5601012011500"))
