import pandas
import ast


class Converter:

    def convert_to_xls(self):
        pass


class JsonConverter(Converter):

    def convert_to_xls(self):
        with open('resources/students.txt', 'r', encoding='utf-8') as f:
            student_json = f.read()
            pandas.read_json(student_json).T.to_excel('students.xlsx')  # row to column
            # pandas.read_json(student_json).T.to_excel('students.xlsx') column to row


class DictConverter(Converter):

    def convert_to_xls(self):
        with open('resources/city.txt', 'r', encoding='utf-8') as f:
            city_dict = ast.literal_eval(f.read()) # Convert string to dict
            pandas.DataFrame.from_dict(city_dict, orient='index').to_excel('resources/city.xlsx')


if __name__ == '__main__':
    c = DictConverter()
    c.convert_to_xls()