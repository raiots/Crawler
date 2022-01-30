import requests
from bs4 import BeautifulSoup
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}

for i in range(1000, 20000):
    try:
        i = str(i)
        url = "http://www.zxcs.me/download.php?id=" + i
        print(i)

        # 获取标题正文页数据
        page_text = requests.get(url, headers=headers).text
        soup = BeautifulSoup(page_text, 'html.parser')
        # 解析获得标签
        ele = soup.find('span', class_='downfile')
        content = ele.a['href']  # 获取标签中的数据
        os.system('wget ' + '\'' + content + '\'')
        time.sleep(5)


        print(content)
    except Exception as e:
        pass
    continue
