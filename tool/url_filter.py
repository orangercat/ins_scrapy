import re
from sys import argv
from collections import Counter


filename = argv[1]
pattern = re.compile(r'[a-zA-z]+://[^\s]*/')


def urls_re(filename):
    with open(filename + '.txt', 'r') as in_file:
        with open(filename + '_url.txt', 'w') as out_file:
            urls = in_file.readlines()
            print(in_file.readlines())
            # for i in in_file.readlines():
            #     url_re = re.findall(pattern, i)
            #     urls.append(url_re)
            urls_counter = Counter(urls)
            print(urls_counter)
            for url_counter in urls_counter:
                out_file.write(url_counter)


if __name__ == "__main__":
    urls_re(filename)
