from scrappers import continente, auchan, gsoares, elcorteingles, ptvineyards, garrafinhas
from sqlalchemy import create_engine, text
from utils.logger import logger, log
from utils.time import get_current_timestamp
from database import db

connection_string = "mysql+mysqlconnector://sogrape:hackaton42sogrape@127.0.0.1:3306/sogrape"
engine = create_engine(connection_string, echo=True)

# TODO marked to delete
# urls = {
# 	"Continente" : "https://www.continente.pt/pesquisa/?q=",
# 	"auchan" : "https://www.auchan.pt/pt/pesquisa?q=",
# 	"gsoares" : "https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=",
# 	"El Corte Ingls" : "https://www.elcorteingles.pt/supermercado/pesquisar/?term=",
# 	"portugalvineyards" : "https://www.portugalvineyards.com/pt/search?s=",
# 	"garrafinhas" : "https://garrafinhas.pt/?s="
# }


# ----------------------- Dict with scrapper functions ----------------------- #
scrapper_dict = {
    1: continente.scrapper,
    2: elcorteingles.scrapper,
	3: gsoares.scrapper,
}

def	main():

	with engine.connect() as connection:
		products = connection.execute(text("SELECT * FROM products"))
		stores = connection.execute(text("SELECT * FROM stores"))

	stores = list(stores.mappings())

	for product in products.mappings():
		print("\nEAN:", product["id"],"Product:" , product["name"], "Brand:", product["brand"])
		for store in stores:
			# reset entry
			entry = None

			# Make sure the scrapper is in the scprapper_dict
			if scrapper_dict.get(store['id']) == None:  
				logger(log.CRITICAL, f"Store ID {store['id']} {store['name']} has no scrapper in the dictionary!") 
				continue
			
			# Use the store scrapper, if exception is thrown, continue to the next store
			try:
				entry = scrapper_dict[store['id']](product["id"], store["search_url"])
			except:
				logger(log.ERROR , f"Scrapper {store['name']} for product {product['name']} and EAN {product['id']} failed!")
				continue

			if not entry:
				logger(log.INFO, f"{product['id']} was not found in {store['name']}")
				continue	

			# update the rest of the columns
			entry["created_at"] = get_current_timestamp()
			entry["updated_at"] = get_current_timestamp()
			entry["ean"] = product["id"]
			entry["store_id"] = store["id"]

			db.insert_entry(entry)
			
		logger(log.INFO, f"{product['id']} {product['name']} finished scrapping!")


if __name__ == "__main__":
    main()
