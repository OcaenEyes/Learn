import requests

def get_one_page(url):
    headers ={

        'Host': 'maoyan.com',
        'Cookie':'uuid=1A6E888B4A4B29B16FBA1299108DBE9C4B0881A83E06E64D4F9D385E24208E8B; _csrf=aa038eff83f5ab231ddfc0456361a1f35fc8ba1734fb65be7b28add28f588e82; _lxsdk_cuid=1643b490850c8-0013fc592b8a27-17356953-13c680-1643b490851c8; __mta=45947547.1530002999573.1530002999573.1530002999573.1; _lxsdk=1A6E888B4A4B29B16FBA1299108DBE9C53832F25B52A78F4A73106CCEAACD770; _lxsdk_s=1643b490851-c62-422-e5d%7C%7C10',
        'User - Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()