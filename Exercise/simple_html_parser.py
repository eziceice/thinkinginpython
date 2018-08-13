from bs4 import BeautifulSoup


def parse_html(resource):
    soup = BeautifulSoup(resource, features='html.parser')
    print(soup.get_text())
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == '__main__':
    file = open('resources/Aries.html')
    f = file.read()
    parse_html(f)