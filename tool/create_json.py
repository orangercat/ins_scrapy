import json
from sys import argv

filename = argv[1]

with open(filename + '.json', 'r') as json_file:

    with open(filename + '_new.json', 'w') as json_file_new:

        json_file_new.truncate()

        datas = json.load(json_file)

        for data in datas:

                # print(url['url'])
            del data['url']

        json.dump(datas, json_file_new, indent=1)
