from scrappers import continente, auchan, gsoares, elcorteingles, ptvineyards

urls = {
	"continente" : "https://www.continente.pt/pesquisa/?q=",
	"auchan" : "https://www.auchan.pt/pt/pesquisa?q=",
	"gsoares" : "https://www.garrafeirasoares.pt/pt/resultado-da-pesquisa_36.html?term=",
	"elcorteingles" : "https://www.elcorteingles.pt/supermercado/pesquisar/?term=",
	"portugalvineyards" : "https://www.portugalvineyards.com/pt/search?s="
}


def	main():
	# product = continente.scrapper("5601012004427", urls["continente"])
	# product = auchan.scrapper("5601012004427", urls["auchan"])
	# product = gsoares.scrapper("5601012004427", urls["gsoares"])
	# product = elcorteingles.scrapper("5601012004427", urls["elcorteingles"])
	product = ptvineyards.scrapper("5601012004427", urls["portugalvineyards"])
	print(product)

if __name__ == "__main__":
    main()
