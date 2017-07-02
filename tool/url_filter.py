import re
from sys import argv
from collections import Counter


filename = argv[1]
pattern = re.compile(r'[a-zA-z]+://[^\s]*/')


def urls_re(filename):
    with open(filename + '.txt', 'r') as txt_file:
        with open(filename + '_url.txt', 'w') as url_file:
            for url in txt_file:
                urls_re = re.findall(pattern, url)
                urls_re_counter = Counter(urls_re)
                # print(urls_re_counter)
                for url_re_counter in urls_re_counter:
                    # print(url_re_counter)
                    # for url_re in urls_re:
                    url_file.write(url_re_counter + '\n')


if __name__ == "__main__":
    urls_re(filename)
