from urllib import request
import re
p = re.compile('google')
text = request.urlopen('http://www.google.com').readline()
text = bytes.decode(text)
print(p.findall(text).__sizeof__())