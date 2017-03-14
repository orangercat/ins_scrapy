import scrapy
# import re
import json

# from .. import items
from . import inscityspider


# Inheritance class InsCitySpider
class InsLocationSpider(inscityspider.InsCitySpider):
    name = 'InsIndiaLocation'
    allowed_domains = ['instagram.com']

    def start_requests(self):
        with open('city.json', 'r') as f:
            citys = json.load(f)
        for city in citys:
            yield scrapy.Request(city['url'], self.parse)
