import scrapy

class BookSpider(scrapy.Spider):
    name = 'book-spider'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):

        # Find each book, iterate and yield
        for one_book in response.css('article.product_pod'):

            title_text = one_book.css('h3 > a::text').extract_first()
            price = one_book.css('p.price_color::text').extract_first()

            yield {'title':title_text,
                   'price':price}

        # Find the "next" button, and yield that for additional scraping
        next_page = response.css('.next > a:nth-child(1)').extract_first()

        if next_page:   # if there is a next_page button...
            yield scrapy.Request(response.urljoin(next_page))
