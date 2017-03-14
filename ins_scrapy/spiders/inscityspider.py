import scrapy
# import re
# import json

from .. import items


class InsCitySpider(scrapy.Spider):
    name = 'InsIndiaCity'
    allowed_domains = ['instagram.com']
    start_urls = ['https://www.instagram.com/explore/locations/IN/india/']

    def parse(self, response):
        # xpath script for sharedData value and json data
        # javascript = "".join(response.xpath('//script[contains(text(), "sharedData")]/text()').extract())
        # json_data = json.loads("".join(re.findall(r'window._sharedData = (.*);', javascript)))
        # data = json_data['entry_data']['LocationsDirectoryPage']
        # city_list = data[0]['city_list']
        city_list = response.xpath('//body//main//a/@href').extract()
        base_url = 'https://www.instagram.com'
        citys = []
        for city in city_list:
            item = items.InsScrapyItem()
            item['url'] = base_url + city
            citys.append(item)
            yield item

        # return citys
        # search page and parse again
        page_url = ''.join(response.xpath("//body//main//a[contains(@href,'page')]/@href").extract())
        if page_url == '':
            return
        else:
            next_url = base_url + page_url
            yield scrapy.Request(next_url, callback=self.parse)
