import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        # this method should look for one or more values in the
        # response, using CSS selectors.

        for one_quote in response.css('div.quote'):
            yield one_quote
