from scrappers import continente, auchan, gsoares, elcorteingles, ptvineyards, garrafinhas, coop, generic
from sqlalchemy import create_engine, text
from utils.logger import logger, log
from utils.time import get_current_timestamp
from utils.parser import extract_year_from_str
from database import db

connection_string = "mysql+mysqlconnector://sogrape:hackaton42sogrape@127.0.0.1:3306/sogrape"
engine = create_engine(connection_string, echo=True)

# ----------------------- Dict with scrapper functions ----------------------- #
scrapper_dict = {
    1: continente.scrapper,
    2: elcorteingles.scrapper,
    3: gsoares.scrapper,
    4: auchan.scrapper,
    5: garrafinhas.scrapper,
    6: ptvineyards.scrapper,
    7: coop.scrapper,
}


def main():
    with engine.connect() as connection:
        products = connection.execute(text("SELECT * FROM products"))
        stores = connection.execute(text("SELECT * FROM stores"))

    stores = list(stores.mappings())

    for product in products.mappings():
        print("\n-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------")
        print(f'\n|EAN: {product["id"]} | Product: {product["name"]}  | Brand: {product["brand"]}')
        for store in stores:
            # reset entry
            entry = None

            if store['use_generic']:
                logger(log.DEBUG, f"Using generic scrapper for store: {store['name']}!!")

                entry = generic.scrapper(store, product["id"])
                if entry is None:
                    logger(log.ERROR,
                           f"Scrapper {store['name']} for product {product['name']} and EAN {product['id']} failed with generic scrapper!")
                # try:
                # except:
                #     logger(log.ERROR,
                #     continue

            else:
                # Make sure the scrapper is in the scrapper_dict
                if scrapper_dict.get(store['id']) is None:
                    logger(log.CRITICAL, f"Store ID {store['id']} {store['name']} has no scrapper in the dictionary!")
                    # continue
                # Use the store scrapper, if exception is thrown, continue to the next store
                # try:
                #     entry = scrapper_dict[store['id']](product["id"], store["search_url"])
                # except:
                #     logger(log.ERROR,
                #            f"Scrapper {store['name']} for product {product['name']} and EAN {product['id']} failed!")
                #     continue

            if not entry:
                logger(log.INFO, f"{product['id']} was not found in {store['name']}")
                continue

            # update the rest of the columns
            entry["created_at"] = get_current_timestamp()
            entry["updated_at"] = get_current_timestamp()
            entry["ean"] = product["id"]
            entry["store_id"] = store["id"]
            entry["year"] = extract_year_from_str(entry['name'])

            logger(log.DEBUG, f" Insert DB -- {entry['name']} {entry['year']} --")
            db.insert_entry(entry)
        logger(log.INFO, f"{product['id']} {product['name']} finished scrapping!")
    print("\n---------------------------------------| Scraper has finished |-------------------------------------------\n")


if __name__ == "__main__":
    main()
