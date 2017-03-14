import json

filename = 'picaram'

json_file = open(filename + '.json', 'r')

txt_file = open(filename + '.txt', 'w')

url_datas = json.load(json_file)

for url in url_datas:

    # print(url['url'])

    txt_file.write(url['url'] + '\n')

json_file.close()

txt_file.close()
