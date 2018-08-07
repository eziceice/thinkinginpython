from random import *
import string


def generate(break_digits, code_length):
    """
    Generate the discount code
    :param break_digits: digits that need to add _
    :param code_length: the total length of the discount code
    :return:
    """
    alphabet_digits = string.ascii_letters + string.digits
    raw_code = ''.join(choices(alphabet_digits, k=code_length))
    code = '-'.join([raw_code[i:i + break_digits] for i in range(0, len(raw_code), break_digits)])
    return code


if __name__ == '__main__':
    list = []
    for i in range(200):
        list.append(generate(4, 16))
    print(list)