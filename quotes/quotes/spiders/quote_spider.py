import scrapy

class QuoteSpider(scrapy.Spider):

    name = "quotebot"

    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").get(),
                'author': quote.css("small.author::text").get(),
                'tags': quote.css("div.tags > a.tag::text").get() 
            }
        
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))