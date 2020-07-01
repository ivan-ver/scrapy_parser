from pprint import pprint

import scrapy
from pars.items import Article


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    start_urls = ['https://javadevblog.com/category/java/nachalo-raboty']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):

        urls = response.xpath("//h2[@class='entry-title']/a/@href").extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_art)

    def parse_art(self, response):
        art = Article()
        art['title'] = response.xpath("//h1[@class='entry-title ']/text()").get()
        art['author'] = response.xpath("//span[@class='author vcard']/a/text()").get()
        art['p_date'] = response.xpath("//span[@class='posted-on']/a/time/text()").get()
        tags = ''
        for tag in response.xpath("//span[@class='cat-links']/a/text()").extract():
            tags += tag+','
        art['tags'] = tags[:-1]
        yield art

