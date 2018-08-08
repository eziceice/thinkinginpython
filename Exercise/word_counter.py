import re
import collections


def read_file(path):
    file = open(path, 'r', encoding='utf-8')
    result = re.sub(r'[^a-zA-Z0-9 \n\.]', '', file.read()).split(' ')
    words = collections.Counter(result)
    for key, val in words.items():
        print(key, val)


if __name__ == '__main__':
    read_file('resources/words.txt')