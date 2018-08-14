import pandas

with open('resources/students.txt', 'r', encoding='utf-8') as f:
    student_json = f.read()
    pandas.read_json(student_json).T.to_excel('students.xlsx')  # row to column
    # pandas.read_json(student_json).T.to_excel('students.xlsx') column to row
