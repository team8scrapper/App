from scrappers import continente, auchan, gsoares, elcorteingles, ptvineyards, garrafinhas
from sqlalchemy import create_engine, text
import datetime

connection_string = "mysql+mysqlconnector://sogrape:hackaton42sogrape@10.18.207.213:3306/sogrape"
engine = create_engine(connection_string, echo=True)

urls = {
	"Continente" : "https://www.continente.pt/pesquisa/?q=",
	"auchan" : "https://www.auchan.pt/pt/pesquisa?q=",
	"gsoares" : "https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=",
	"El Corte Ingls" : "https://www.elcorteingles.pt/supermercado/pesquisar/?term=",
	"portugalvineyards" : "https://www.portugalvineyards.com/pt/search?s=",
	"garrafinhas" : "https://garrafinhas.pt/?s="
}

def	main():
	with engine.connect() as connection:
		products = connection.execute(text("SELECT * FROM products"))
		stores = connection.execute(text("SELECT * FROM stores"))

	# Get the current timestamp
	timestamp = datetime.datetime.now()
	# Format the timestamp as a string in the MySQL-compatible format
	mysql_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
	
	for product in products.mappings():
		# Current Product
		print("\nEAN:", product["id"],"Product:" , product["name"], "Brand:", product["brand"])
		for store in stores.mappings():
			if store["id"] == 1
				current = continente.scrapper(product["id"], store["search_url"])
			elif store["id"] == 2 
				current = elcorteingles.scrapper(product["id"], store["search_url"])
			elif store["id"] == 3 
				current = gsoares.scrapper(product["id"], store["search_url"])
			if not current:
				continue	
			current["created_at"] = mysql_timestamp
			current["updated_at"] = mysql_timestamp
			current["ean"] = product["id"]
			current["store_id"] = store["id"]
			sql = text("INSERT INTO product_entries (created_at, updated_at, price, url, product_id, store_id, product_name, currency) VALUES (:created_at, :updated_at, :price, :url, :ean, :store_id, :name, :currency)")


if __name__ == "__main__":
    main()
