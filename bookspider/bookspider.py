import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        for one_quote in response.css('article.product_pod'):
            # quote_text = one_quote.css('.text::text').extract_first()
            # author_name = one_quote.css('.author::text').extract_first()

            # yield {'text': quote_text,
            #        'author':author_name}

            yield {}
