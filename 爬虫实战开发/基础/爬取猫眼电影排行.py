import requests
import re
import json
from requests.exceptions import RequestException
import time

# 获取单独一个页面
def get_one_page(url):
    try:
        headers ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return  response.text
    except RequestException:
        return None

#解析一个页面
#此处正则判断为难点，需要仔细研读
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+ item[6],
        }


#写入文件
def write_to_json(content):
    with open ('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

#分页读取
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset = i *10)
        time.sleep(2)
