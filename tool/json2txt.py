import json
from sys import argv

filename = argv[1]

json_file = open(filename + '.json', 'r')

txt_file = open(filename + '.txt', 'w')

txt_file.truncate()

url_datas = json.load(json_file)

for url in url_datas:

    # print(url['url'])

    txt_file.write(url['url'] + '\n')

json_file.close()

txt_file.close()
