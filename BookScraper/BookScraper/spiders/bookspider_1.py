import scrapy


class Bookspider1Spider(scrapy.Spider):
    name = "bookspider-1"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
