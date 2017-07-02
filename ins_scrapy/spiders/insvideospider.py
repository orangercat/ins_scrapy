# -*- coding=UTF-8 -*-
import scrapy
import re
import json
from .. import items
# import requests
# from scrapy.selector import Selector
from scrapy.conf import settings

# from scrapy.http import Request, FormRequest
# from scrapy.http.cookies import CookieJar


class InsSpider(scrapy.Spider):
    name = 'InsVideo'
    allowed_domains = ['instagram.com']
    cookie = settings['COOKIE']  # read cookie from setting

    # start_urls = ['https://www.instagram.com/explore/locations/216524182/amity-universitynoida/']

    # def start_requests(self):
    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    # yield Request(self.start_urls[0], callback=self.parse,
    # cookies=self.cookie)
    def start_requests(self):
        with open('location.json', 'r') as f:
            locations = json.load(f)
        for location in locations:
            yield scrapy.Request(location['url'], callback=self.parse, cookies=self.cookie)

    def parse(self, response):
        # self.logger.info('start_urls %s', self.start_urls[0])
        # xpath script for sharedData value and json data
        # javascript = Selector(text=response).xpath('//script[contains(text(), "sharedData")]/text()').extract()
        javascript = "".join(response.xpath('//script[contains(text(), "sharedData")]/text()').extract())
        json_data = json.loads("".join(re.findall(r'window._sharedData = (.*);', javascript)))
        '''
        node sample
        {'code': 'BRgugwTgkDs',
         'comments': {'count': 0},
         'comments_disabled': False, 'date': 1489264324,
         'dimensions': {'height': 800,'width': 640},
         'display_src': 'https://scontent-dft4-2.cdninstagram.com/1.jpg',
         'id': '1468378039552458988','is_video': False,
         'likes': {'count': 8},
         'owner': {'id': '1561263483'},
         'thumbnail_src': 'https://scontent-dft4-2.cdninstagram.com/8730221800278982656_n.jpg'},
        '''
        # nodes_data = json_data['entry_data']['LocationsPage'][0]['location']['media']['nodes']
        top_post_nodes_data = json_data['entry_data']['LocationsPage'][0]['location']['top_posts']['nodes']
        # nodes_data.extend(top_post_nodes_data)
        taken_at = json_data['entry_data']['LocationsPage'][0]['location']['id']
        # self.logger.info('nodes_data %s', nodes_data)
        # videos = []
        for node in top_post_nodes_data:
            # self.logger.info('node %s', node)

            item = items.InsScrapyItem()
            if node['is_video'] and node['comments']['count'] + node['likes']['count'] > 1000:
                # self.logger.info('node %s', node['code'])
                # self.logger.info('comment %s', node['comments']['count'])
                # self.logger.info('likes %s', node['likes']['count'])
                # print(node['code'])
                item['url'] = 'https://www.instagram.com/p/' + node['code'] + '/?taken-at=' + taken_at
                item['comments_count'] = node['comments']['count']
                item['likes_count'] = node['likes']['count']
                # videos.append(item)
                yield item
            else:
                pass
