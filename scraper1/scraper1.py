import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    start_urls = ['https://quotes.toscrape.com']
