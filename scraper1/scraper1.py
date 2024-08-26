import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quote-spider'
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        # this method should look for one or more values in the
        # response, using CSS selectors.

        for one_quote in response.css('div.quote'):
            # grab the item with a "text" class (i.e., .text)
            # grab the text from within the text (i.e., ::text)
            quote_text = one_quote.css('.text::text').extract_first()

            yield {'text': quote_text}
