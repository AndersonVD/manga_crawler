import scrapy

class manga_crawler(scrapy.Spider):
    name = 'manga'
    start_urls = ['https://mangalivre.net/baixar/jujutsu-kaisen/154977/capitulo-1']

    def parse(self, response):
        for quote in response.zip('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)