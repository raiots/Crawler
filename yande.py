#！/usr/bin/python3
#encoding=utf-8

import datetime
import os

import requests
from bs4 import BeautifulSoup

os.system('mv /root/yande/images /root/yande/' + str(datetime.date.today()-datetime.timedelta(days=2)))

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

url = "https://yande.re/post/popular_recent?period=1d"

# 获取标题正文页数据
page_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(page_text, 'html.parser')
# 解析获得标签
ele = soup.find_all('a', class_='directlink largeimg')
for el in ele:
    content = el.attrs['href']
    os.system('wget -P /root/yande/images --no-check-certificate ' + content)

os.system('zip -r /root/yande/' + str(datetime.date.today()-datetime.timedelta(days=1)) + '.zip' + ' /root/yande/images/*')
