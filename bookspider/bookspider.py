import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        for one_book in response.css('article.product_pod'):


            title_text = one_book.css('h3 > a').extract_first()
            price = one_book.css('p.price-color').extract_first()

            yield {'title':title_text,
                   'price':price}
