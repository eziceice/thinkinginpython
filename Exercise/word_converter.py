import pandas
import ast
from dicttoxml import dicttoxml


class Converter:

    def convert_to_xls(self, path):
        pass

    def open_file(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def convert_to_xml(self, path):
        pass


class JsonConverter(Converter):

    def convert_to_xls(self, path):
        students_json = super().open_file(path)
        pandas.read_json(students_json).T.to_excel('students.xlsx')  # row to column
        # pandas.read_json(student_json).T.to_excel('students.xlsx') column to row


class DictConverter(Converter):

    def convert_to_xls(self, path):
        citys = super().open_file(path)
        city_dict = ast.literal_eval(citys)  # Convert string to dict
        pandas.DataFrame.from_dict(city_dict, orient='index').to_excel('resources/city.xlsx')


class ListConverter(Converter):

    def convert_to_xls(self, path):
        numbers = super().open_file(path)
        number_list = ast.literal_eval(numbers)  # Convert string to list
        pandas.DataFrame(number_list).to_excel('resources/numbers.xlsx')


class XLSXConverter(Converter):

    def convert_to_xml(self, path, mode='w'):
        items = pandas.read_excel(path).to_json()
        items = ast.literal_eval(items)
        self.rename_tag(items)
        for valus in items.values():
            self.rename_tag(valus)
        items_xml = dicttoxml(items, custom_root='items', attr_type=False).decode('utf-8')
        with open('resources/items.xml', 'w', encoding='utf-8') as f:
            f.write(items_xml)

    def rename_tag(self, items):
        for key in items.keys():
            items['item{}'.format(key)] = items.pop(key)


if __name__ == '__main__':
    xlsx = pandas.read_excel('resources/test.xls', usecols='C')
    print(xlsx.get_values().sum())