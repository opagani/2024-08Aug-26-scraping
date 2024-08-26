import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):


        for one_quote in response.css('div.quote'):
            # grab the item with a "text" class (i.e., .text)
            # grab the text from within the text (i.e., ::text)
            quote_text = one_quote.css('.text::text').extract_first()
            author_name = one_quote.css('.author::text').extract_first()

            yield {'text': quote_text,
                   'author':author_name}
