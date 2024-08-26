import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        for one_book in response.css('li.col-xs-6:nth-child(1) > article:nth-child(1) > h3:nth-child(3) > a:nth-child(1)'):


            title_text = one_book.css('a').extract_first()
            # author_name = one_quote.css('.author::text').extract_first()

            # yield {'text': quote_text,
            #        'author':author_name}

            yield {'title':title_text}
