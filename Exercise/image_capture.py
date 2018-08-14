from urllib import request
from bs4 import BeautifulSoup


def download_image(url):
    req = request.urlopen(url)
    soup_html = BeautifulSoup(req.read(), features='html.parser')
    images = soup_html.find_all('img')
    links = [each.get('src') for each in images]
    for each in links:
        filename = each.strip().split('/')[-1].strip()
        file_path = 'resources/' + filename
        request.urlretrieve(url + each, file_path)


if __name__ == '__main__':
    url = 'https://www.google.com'
    download_image(url)

