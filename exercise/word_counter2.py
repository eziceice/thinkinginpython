import os
import os.path
import re
import collections


def find_doc(root_dir):
    for parent, dir, files in os.walk(root_dir): # dir是所有文件夹的名字, files是所有文件的名字, root表示当前目录的父目录
        for file in files:
            if file.endswith('.txt'):
                word_counter('{}/{}'.format(parent, file))


def word_counter(file_path):
    file = open(file_path, 'r', encoding='utf-8')
    result = re.sub(r'[^a-zA-Z0-9 \n\.]', '', file.read()).split(' ')
    words = collections.Counter(result)
    max_key = max(words, key=words.get)
    print(max_key, words[max_key])


if __name__ == '__main__':
    find_doc('resources')