from scrappers import continente

def	main():
	product = continente.scrapper("5601012004427", "https://www.continente.pt/pesquisa/?q=")
	print(product)

if __name__ == "__main__":
    main()
