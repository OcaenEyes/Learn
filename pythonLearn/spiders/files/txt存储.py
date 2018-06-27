import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers={
'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'

}
html = requests.get(url,headers = headers).text
print(html)
doc = pq(html)
print(doc)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer =pq(item.find('.content').html()).text()
    file = open('zhihu.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n'+ '='*50 +'\n')
    file.close()

