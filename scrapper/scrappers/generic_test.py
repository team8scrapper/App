import pytest
from generic import get_product_url, get_product_content, get_product_details, scrapper

products = [
	scrapper("https://www.continente.pt", "https://www.continente.pt/pesquisa/?q=", "5601012011500", ".results-section .product a", {
		"name": ".product-name-details .product-name",
		"price": ".product-name-details .ct-price-formatted",
	}),
	scrapper("https://www.auchan.pt", "https://www.auchan.pt/pt/pesquisa?q=", "5601012011500", ".product-grid .auc-product a", {
		"name": ".auc-pdp__header .product-name",
		"price": ".product-detail .price .value",
	}),
	scrapper("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "5601012011500", "main article.product a", {
		"name": ".product-main .product-title",
		"price": ".product-main .product-page-price .woocommerce-Price-amount.amount bdi"
	}),
	scrapper("https://www.portugalvineyards.com/pt", "https://www.portugalvineyards.com/pt/search?controller=search&s=", "5601012011500", ".products article.product-miniature a", {
		"name": ".ttvproduct-details-page .ttvproduct-detail-title",
		"price": ".product-prices .current-price .ttvpopup-carrent-price"
	})
]

def test_products_details():
	assert products[0] == {'name': 'Mateus Vinho Rosé', 'description': '', 'price': 4.49, 'currency': 'EUR', 'url': 'https://www.continente.pt/produto/mateus-vinho-rose-mateus-2050174.html'}
	assert products[1] == {'name': 'vinho rosé mateus 0.75l', 'price': 4.49, 'url': 'https://www.auchan.pt/pt/bebidas-e-garrafeira/garrafeira/vinhos-rose/douro-rose/vinho-rose-mateus-0.75l/38534.html', 'description': '', 'currency': 'EUR'}
	assert products[2] == {'name': '\tMateus Rose', 'price': 4.25, 'url': 'https://garrafinhas.pt/produto/mateus-rose/', 'description': '', 'currency': 'EUR'}
	assert products[3] == {'name': 'Mateus Rosé Original', 'price': 5.15, 'url': 'https://www.portugalvineyards.com/pt/portugal/1278-mateus-rose-original-5601012011500.html', 'description': '', 'currency': 'EUR'}


# print(scrapper("https://www.auchan.pt", "https://www.auchan.pt/pt/pesquisa?q=", "5601012011500", ".product-grid .auc-product a", {
# 		"name": ".auc-pdp__header .product-name",
# 		"price": ".product-detail .price .value",
# 	}),)






# print(get_product_url("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "5601012011500", "main article.product a"))

# def test_products_in_store():
# 	assert product_links[0] == "https://www.continente.pt/produto/mateus-vinho-rose-mateus-2050174.html"
# 	assert product_links[1] == "https://www.auchan.pt/pt/bebidas-e-garrafeira/garrafeira/vinhos-rose/douro-rose/vinho-rose-mateus-0.75l/38534.html"
# 	assert product_links[2] == "https://garrafinhas.pt/produto/mateus-rose/"
	
# def test_products_not_store():
# 	assert get_product_url("https://www.continente.pt", "https://www.continente.pt/pesquisa/?q=", "asdhdjsdfg", ".results-section .product a") == None
# 	assert get_product_url("https://www.auchan.pt", "https://www.auchan.pt/pt/pesquisa?q=", "asdhdjsdfg", ".product-grid .auc-product a") == None
# 	assert get_product_url("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "asdhdjsdfg", "main article.product a") == None
