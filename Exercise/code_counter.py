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
    comments = 0
    codings = 0
    totallines = 0
    codes = open(file_path, 'r', encoding='utf-8')

    while True:
        line = codes.readline()
        totallines += 1
        if not line:
            break
        elif line.strip().startswith('#'):
            comments += 1
        elif line.strip().startswith("'''") or line.strip().startswith('"""'):
            comments += 1
            while True:
                line = codes.readline()
                totallines += 1
                comments += 1
                if ("'''" in line) or ('"""' in line):
                    break
        elif line.strip():
            codings += 1
        else:
            blank += 1

    print(file_path, totallines, blank, comments, codings)


if __name__ == '__main__':
    all_files = find_files('../Exercise')
    for file in all_files:
        count_codes(file)