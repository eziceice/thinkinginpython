
def filter_word(path):
    with open(path, 'r', encoding='utf-8') as f:
        words = f.readlines()
        words = [s.strip() for s in words]
        return words


if __name__ == '__main__':
    words = filter_word('resources/filtered_words.txt')
    while True:
        text = input('Please enter a word:')
        # if text in words:
        #     print('Freedom')
        # elif text == 'exit':
        #     print('Exit')
        #     exit()
        # else:
        #     print('Human Rights')
        for word in words:
            if word in text:
                text = text.replace(word, len(word) * '*')
        print(text)
