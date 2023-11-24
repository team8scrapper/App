from scrappers import continente, auchan, gsoares, elcorteingles, ptvineyards, garrafinhas

urls = {
	"continente" : "https://www.continente.pt/pesquisa/?q=",
	"auchan" : "https://www.auchan.pt/pt/pesquisa?q=",
	"gsoares" : "https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=",
	"elcorteingles" : "https://www.elcorteingles.pt/supermercado/pesquisar/?term=",
	"portugalvineyards" : "https://www.portugalvineyards.com/pt/search?s=",
	"garrafinhas" : "https://garrafinhas.pt/?s="
}

# 5601012002515

def	main():
	ean = "5601012002515"
	#product = continente.scrapper(ean, urls["continente"])
	#print(product)
	#product = auchan.scrapper(ean, urls["auchan"])
	#print(product)
	product = gsoares.scrapper(ean, urls["gsoares"])
	print(product)
	product = elcorteingles.scrapper(ean, urls["elcorteingles"])
	print(product)
	product = ptvineyards.scrapper(ean, urls["portugalvineyards"])
	print(product)
	#product = garrafinhas.scrapper("5601012004427", urls["garrafinhas"])
	#print(product)

if __name__ == "__main__":
    main()
