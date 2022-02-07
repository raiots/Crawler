# !/usr/bin/python3
# encoding=utf-8

import time
import os

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

base_url = "https://kemono.party"
user = "https://kemono.party/patreon/user/15873007"
pages = input("How many pages do you want to scrape：")

# requests不走代理 https://stackoverflow.com/questions/28521535/requests-how-to-disable-bypass-proxy
session = requests.Session()
session.trust_env = False


def crawl_page(page_url):
    # 获取标题正文页数据
    page_text = session.get(page_url, headers=headers).text
    soup = BeautifulSoup(page_text, 'html.parser')

    # 解析获得标签
    ele = soup.find_all('h2', class_='post-card__heading')
    for el in ele:
        entry_url = base_url + el.find('a').attrs['href']

        time.sleep(2)
        entry = BeautifulSoup(session.get(entry_url, headers=headers).text, 'html.parser')
        attachment_urls = entry.find_all('a', class_='post__attachment-link')
        for attachment_url in attachment_urls:
            file = base_url + attachment_url.attrs['href']

            # for filter
            # if(file.find("4K")!=-1):
            #     print(file)

            print(file)


for i in range(int(pages)):
    page_url = user + "?o=" + str(i*25)
    crawl_page(page_url)
