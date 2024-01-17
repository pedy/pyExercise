# Based on the sample on https://docs.scrapy.org/en/latest/intro/overview.html
import scrapy

siteURL = 'https://www.merriam-webster.com'
class WordsSpider(scrapy.Spider):
    name = "words"
    start_urls = [
        siteURL + "/wordfinder/classic/begins/all/5/a/1",
    ]

    def parse(self, response):
        for word in response.css("li.pb-4 > a::text"):
            yield {word.root: ""}

        if len(response.css('.next > a')) > 0:
            next_page = siteURL + response.css('.next > a').attrib['href']
        else:
            next_page = None
        #print(f'Next page: {next_page}')
        if next_page is not None:
            yield response.follow(next_page, self.parse)
