import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        for one_book in response.css('article.product_pod'):
            title_text = one_book.css('a').extract_first()
            # author_name = one_quote.css('.author::text').extract_first()

            # yield {'text': quote_text,
            #        'author':author_name}

            yield {'title':title_text}
