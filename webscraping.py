import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

product_name = []
price_list = []
quantity_list = []
discount_list = []


url = "https://www.continente.pt/bebidas-e-garrafeira/vinhos/?start=0&srule=FOOD-Bebidas&pmin=0.01"

for i in range(1, 3):

	r = request.get(url)
	soup = BeautifulSoup(r.text, "lxml")

	block = soup.find_all("div", class_ = "col-12 col-sm-3 col-lg-2 productTile")

blocks = []

for i in block:
	name_final = i.find("a", class_ = "pwc-tile--description col-tile--description")
	if (name_final == None):
		name = "n/a"
	else:
		name = name_final.text
	product_name.append(name)

	price = i.find("span", class_ = "value").get("content")
	price_list.append(price)

	quantity_final = i.find("p", class_ = "pwc-tile--quantity col-tile--quantity")
	if (quantity_final == None):
		quantity = "n/a"
	else:
		quantity = quantity_final.text
	quantity_list.append(quantity)

	discount_final = i.find("span", class_ = "ct-product-tile-badge-value--pvpr col-product-tile-badge-value--pvpr")
	if (discount_final == None):
		discount = "n/a"
	else:
		discount = discount_final.text
	discount_list.append(descount.strip("\n \t\r\v"))

df = pd.DataFrame({"Product Name":product_name, "Price": price_list, "Quantity": quantity_list, "Discount": discount_list})
print(df)
