
import scrapy
from quotes_scraper.items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'  
    start_urls = ['http://quotes.toscrape.com/']  # Початкова URL

    def parse(self, response):
       
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('span small.author::text').get()
            item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield item

            author_link = quote.css('span a::attr(href)').get()
            yield response.follow(author_link, self.parse_author)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
      
        author = AuthorItem()
        author['name'] = response.css('h3.author-title::text').get()
        author['birthdate'] = response.css('span.author-born-date::text').get()
        author['bio'] = response.css('div.author-description::text').get()
        yield author
