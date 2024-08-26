import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        for one_book in response.css('article.product_pod'):


            title_text = one_book.css('h3 > a::text').extract_first()
            price = one_book.css('p.price_color::text').extract_first()

            yield {'title':title_text,
                   'price':price}
