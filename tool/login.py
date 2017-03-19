# from userinfo import UserInfo
import requests
from scrapy.selector import Selector
import json
import re


def login():

    url = 'https://www.instagram.com/'
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    test_url = 'https://www.instagram.com/explore/locations/216524182/amity-universitynoida/'
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
    accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
    login = "orangercat@hotmail.com"

    user_login = login.lower()
    user_password = "44087365"
    print('Trying to login as ' + user_login)

    s = requests.Session()

    s.cookies.update({'sessionid': '', 'mid': '', 'ig_pr': '1',
                      'ig_vw': '1920', 'csrftoken': '',
                      's_network': '', 'ds_user_id': ''})
    login_post = {'username': user_login,
                  'password': user_password}
    s.headers.update({'Accept-Encoding': 'gzip, deflate',
                      'Accept-Language': accept_language,
                      'Connection': 'keep-alive',
                      'Content-Length': '0',
                      'Host': 'www.instagram.com',
                      'Origin': 'https://www.instagram.com',
                      'Referer': 'https://www.instagram.com/',
                      'User-Agent': user_agent,
                      'X-Instagram-AJAX': '1',
                      'X-Requested-With': 'XMLHttpRequest'})
    r = s.get(url)
    s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
    login = s.post(url_login, data=login_post,
                   allow_redirects=True)


def parse(requests, url):
    s = requests.Session()
    r = s.get(url)
    s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
    # print(r.text)
    javascript = Selector(text=r.text).xpath(
        '//script[contains(text(), "sharedData")]/text()').extract()
    json_data = json.loads(
        "".join(re.findall(r'window._sharedData = (.*);', javascript[0])))
    top_post_nodes_data = json_data['entry_data'][
        'LocationsPage'][0]['location']['top_posts']['nodes']
    # print(top_post_nodes_data)

    taken_at = json_data['entry_data']['LocationsPage'][0]['location']['id']
    # self.logger.info('nodes_data %s', nodes_data)
    videos = []
    for node in top_post_nodes_data:
        # print(node['comments']['count'])

        if node['is_video'] and node['comments']['count'] + node['likes']['count'] > 0:
            data = {'url': 'https: // www.instagram.com/p/' + node['code'] + '/?taken-at=' + taken_at,
                    'comments_count': node['comments']['count'],
                    'likes_count': node['likes']['count']}
            print(data)

        else:
            pass


if __name__ == "__main__":
    login()
