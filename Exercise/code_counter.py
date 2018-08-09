import os


def find_files(root_dir):
    all_codes = []
    for parent, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                all_codes.append('{}/{}'.format(parent, file))
    return all_codes


def count_codes(file_path):
    blank = 0
    comment = 0
    coding = 0
    codes = open(file_path, 'r', encoding='utf-8').readlines()
    for code in codes:
        code = code.replace('\n', '')
        if not code.strip():
            blank = blank + 1
        elif code.strip().startswith('#'):
            comment = comment + 1
        elif code.strip().startswith('\'') or code.strip().startswith('\"'):
            pass # need to thing another way
        else:
            coding = coding + 1
    print(file_path, blank, comment, coding)


if __name__ == '__main__':
    all_files = find_files('../Exercise')
    for file in all_files:
        count_codes(file)