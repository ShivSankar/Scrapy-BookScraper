import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield{
                'name' : book.css('h3 a::text'),
                'Price' : book.css('.product_price .price_color::text'),
                #'URL' : book.css('h3 a').attrib['href']
            }
