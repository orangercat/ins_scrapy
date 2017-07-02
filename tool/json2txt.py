import json
import re
from sys import argv
from collections import Counter

# json to txt and filter url
filename = argv[1]
pattern = re.compile(r'[a-zA-z]+://[^\s]*/')
with open(filename + '.json', 'r') as json_file:
    with open(filename + '.txt', 'w') as txt_file:
        txt_file.truncate()
        url_datas = json.load(json_file)
        urls = []
        for i in url_datas:

            url_re = re.findall(pattern, i['url'])

            urls.append(url_re[0])

        urls_counter = Counter(urls)
        print(urls_counter)
        for url_counter in urls_counter:
            txt_file.write(url_counter + '\n')
