import scrapy
from ..items import QuotesTutoItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        all = response.css("div.quote")
        items = QuotesTutoItem()
        for i in all:
            q = i.css("span.text::text").extract()
            a = i.css(".author::text").extract()
            t = i.css(".tag::text").extract()

            items["quotes"] = q
            items["author"] = a
            items["tags"] = t
            yield items
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)