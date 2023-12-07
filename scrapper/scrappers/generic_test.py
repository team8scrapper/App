import pytest
from generic import get_page_results, get_product_url


# print(get_product_url("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "5601012011500", "main article.product a"))

def test_products_in_store():
	assert get_product_url("https://www.continente.pt", "https://www.continente.pt/pesquisa/?q=", "5601012011500", ".results-section .product a") == "https://www.continente.pt/produto/mateus-vinho-rose-mateus-2050174.html"
	assert get_product_url("https://www.auchan.pt", "https://www.auchan.pt/pt/pesquisa?q=", "5601012011500", ".product-grid .auc-product a") == "https://www.auchan.pt/pt/bebidas-e-garrafeira/garrafeira/vinhos-rose/douro-rose/vinho-rose-mateus-0.75l/38534.html"
	assert get_product_url("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "5601012011500", "main article.product a") == "https://garrafinhas.pt/produto/mateus-rose/"
	
def test_products_not_store():
	assert get_product_url("https://www.continente.pt", "https://www.continente.pt/pesquisa/?q=", "asdhdjsdfg", ".results-section .product a") == None
	assert get_product_url("https://www.auchan.pt", "https://www.auchan.pt/pt/pesquisa?q=", "asdhdjsdfg", ".product-grid .auc-product a") == None
	assert get_product_url("https://garrafinhas.pt", "https://garrafinhas.pt/?s=", "asdhdjsdfg", "main article.product a") == None
