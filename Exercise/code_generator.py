from random import *
import string
import sqlite3


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


def insert_db(sql, code):
    db = sqlite3.connect('db/yutian_db')
    cursor = db.cursor()
    cursor.execute(sql, (code,))
    db.commit()


def create_db(create_sql):
    try:
        db = sqlite3.connect('db/yutian_db')
        cursor = db.cursor()
        cursor.execute(create_sql)
        db.commit()
    except sqlite3.OperationalError:
        print('Database is already exist, skip creating tables')


if __name__ == '__main__':
    create_sql = 'Create Table codes(id Integer Primary Key, code Text)'
    insert_sql = 'Insert into codes(code) Values(?)'
    create_db(create_sql)
    list = []
    for i in range(200):
        list.append(generate(4, 16))
        insert_db(insert_sql, list[i])
    db = sqlite3.connect('db/yutian_db')
    cursor = db.cursor()
    cursor.execute('select * from codes')
    print(cursor.fetchall())

