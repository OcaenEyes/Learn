import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib import request,error

try:
    html = request.urlopen('https://www.baidu.com')
except error.URLError as e:
    print(e.reason)

from urllib.parse import urlparse

from urllib.parse import urlunparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))