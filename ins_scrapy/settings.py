# -*- coding: utf-8 -*-

# Scrapy settings for ins_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ins_scrapy'

SPIDER_MODULES = ['ins_scrapy.spiders']
NEWSPIDER_MODULE = 'ins_scrapy.spiders'

# 设置Log级别:
LOG_LEVEL = 'DEBUG'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ins_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = False

COOKIE = {
    # '__utma': '227057989.839797024.1489828511.1489828511.1489828511.1',
    # '__utmb':'227057989.2.10.1489828511',
    # '__utmc':'227057989',
    # '__utmt':'1',
    # '__utmz':'227057989.1489828511.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    # 'csrftoken':'jDS81M21YYngsFtKUgKKZLdEeq0hDPZy',
    # 'ds_user_id':'234938809',
    # 'fbm_124024574287414':'base_domain=.instagram.com',
    # 'fbsr_124024574287414':'eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNlbkQ5cnZacWtscFJNS0FUaHpwYkF0dVhPX3B4YzUyaXlTQWFoVmtMOGhrSjUtT3JYWkJxT2lQbmJ4Z2hORUw2a3hLZEdBM1dMLUxfRzd5ZEVaSDhNRW55S1dDTHpScDlZVVQweThTZkQ2TnhrQmhRRk5XZ09PTU16WEtqZmc2RU90R2NoRkc3eEZaUDJtcERxdmdYUUtmUEM2TzlJeEFtaWRISFBsZkV0c3Bxa2RYVFdMZHlTc2pzYXRvSlV1R0pJbmk3NjlibXBRTGZkX21TeTJfSXlXdFlhT0syX2lwWi03UmlZejBMUnRxR2VCc2VTV2ZxbUtBcUxKUU9UNV9OM0UyVUE2NTRIVnlTR0JZNmRaVEdKTFhDSEk5a05mYnEyYlppSGdwZXBUaHcwX0lGQTUyM2JEd0ZTeDY1SzdBaXd0VnBoZUpUdU9Sa2UwYVhNX21VV01vdkdTT0R5YXJmZVlTUU1kTlNsTXciLCJpc3N1ZWRfYXQiOjE0ODk4Mjg1MTIsInVzZXJfaWQiOiIxMDAwMDA0NDk2MjU4MzUifQ',
    # 'ig_lang':'en',
    # 'ig_pr':'2',
    # 'ig_vw':'1280',
    # 'mid':'WLOa4gAEAAFJ3gIapthsfoWUAWPA',
    # 's_network':'""',
    'sessionid': 'IGSC4bc638e76082c6ae9475db2969391f105452d5b8a83b099c3c414939981930dc%3Aoy2THK0rWWrasrWTMY1UfHzvzlmXVY6z%3A%7B%22_auth_user_id%22%3A234938809%2C%22_auth_user_backend%22%3A%22accounts.backends.CaseInsensitiveModelBackend%22%2C%22_auth_user_hash%22%3A%22%22%2C%22_token_ver%22%3A2%2C%22_token%22%3A%22234938809%3Ag2YCUumZe97stWQmZtMB1BBfabRbd5AC%3A42c1662b8ba5607f88e1abe7e8e4b0bbc2f2146ed5e9b6ea088ef9a25049c40f%22%2C%22_platform%22%3A4%2C%22last_refreshed%22%3A1497232919.9351763725%2C%22asns%22%3A%7B%22time%22%3A1497232920%2C%22192.241.227.106%22%3A14061%7D%7D'
}

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ins_scraper.middlewares.InsScraperSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ins_scraper.middlewares.MyCustomDownloaderMiddleware': 543,
# user agen
# 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
# 'ins_scraper.spiders.rotate_useragent.RotateUserAgentMiddleware':400
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'ins_scraper.pipelines.InsScraperPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
