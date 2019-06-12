import json

import requests
import re
from requests.exceptions import RequestException

def get_page(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    try:
        r_html = requests.get(url, headers=header)
        if r_html.status_code == 200:
            return r_html.text
    except RequestException:
        return None


def prase_page(html):
    zz = r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>'
    r = re.compile(zz, re.S)
    all_item = re.findall(r, html)
    for item in all_item:
        yield{
            'index' : item[0],
            'image' : item[1],
            'name' : item[2],
            'star' : item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score' : item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main():
    for i in range(10):
        url = "https://maoyan.com/board/4"
        url_p = '?offset='
        url_s = '0'
        url =url + url_p + str(i) + url_s
        r_html = get_page(url)
        for item in prase_page(r_html):
            write_to_file(item)

if __name__ == "__main__":
    main()
