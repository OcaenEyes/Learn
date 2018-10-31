import requests

response = requests.get('http://detail.zol.com.cn/cpu/index1177026.shtml')

re =response.text
print(re)