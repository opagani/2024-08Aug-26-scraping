# Exercise: Simple Scrapy parser

# Create a directory, and a parser file called bookspider.py.
# Inside of that, create a class that inherits from scrapy.Spider
# Set the name to whatever you want (a string)
# Set the start_urls to a list of one element, the URL 'https://books.toscrape.com/'
# Define the parse method to find the name, author, and price of each book.
# Your parse method should then yield a dict with those three values in it.
# Run the spider from the command line with scrapy runspider bookspider.py
# If you see that you're getting the right values, use -o books.json to write to a JSON file.


import scrapy


class BookSpider(scrapy.Spider):
    name = "book-spider"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # this method should look for one or more values in the
        # response, using CSS selectors.

        for one_book in response.css("article.product_pod"):
            # grab the item with a "text" class (i.e., .text)
            # grab the text from within the text (i.e., ::text)
            name = one_book.css("h3 > a::text").extract_first()
            # author = one_quote.css(".author::text").extract_first()
            price = one_book.css("p.price_color::text").extract_first()

            # yield {}
            yield {"name": name, "price": price}
