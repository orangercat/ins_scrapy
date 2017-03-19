import json
from sys import argv

filename = argv[1]

with open(filename + '.json', 'r') as json_file:

    with open(filename + '.txt', 'w') as txt_file:

        txt_file.truncate()

        url_datas = json.load(json_file)

        for url in url_datas:

                # print(url['url'])

            txt_file.write(url['url'] + '\n')
