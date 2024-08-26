import scrapy


class BookscraperSpiderSpider(scrapy.Spider):
    name = "bookscraper-spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
