import scrapy
from .. import items


class PicaramSpider(scrapy.Spider):
    name = 'Picaram'
    allowed_domains = ['picaram.com']
    start_urls = [
        'http://www.picaram.com/celebrities',
        'http://www.picaram.com/sports',
        'http://www.picaram.com/fashion',
        'http://www.picaram.com/fitness',
        'http://www.picaram.com/animals',
        'http://www.picaram.com/architecture',
        'http://www.picaram.com/arts',
        'http://www.picaram.com/cars',
        'http://www.picaram.com/entertainment',
        'http://www.picaram.com/food',
        'http://www.picaram.com/life',
        'http://www.picaram.com/models',
        'http://www.picaram.com/news',
        'http://www.picaram.com/quotes',
        'http://www.picaram.com/science',
        'http://www.picaram.com/tattoos',
        'http://www.picaram.com/travel',
        'http://www.picaram.com/videos'
    ]

    def parse(self, response):
        video_list = response.xpath(
            '//article//div[@class="content-image video"]/a/@href').extract()
        base_url = 'http://www.Picaram.com'
        videos = []
        for video in video_list:
            item = items.InsScrapyItem()
            item['url'] = base_url + video
            videos.append(item)
            yield item
