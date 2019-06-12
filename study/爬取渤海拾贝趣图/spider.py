import requests
from bs4 import BeautifulSoup
import re, time
from requests.exceptions import RequestException
import lxml

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': 'https://bh.sb/post/category/main/',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Cookie': 'Hm_lvt_2a578e39b75ae053de8b766c8201658e=1559714204; Hm_lpvt_2a578e39b75ae053de8b766c8201658e=1559714598'
}

def get_page(url):
    try:
        r_html = requests.get(url, headers=header)
        if r_html.status_code == 200:
            soup = BeautifulSoup(r_html.content, 'lxml')
            urln = soup.find_all('a', target='_blank')
            pattern = re.compile(r'.*?([a-zA-z]+://[^\s]*)"', re.S)
            result = pattern.findall(str(urln))
            del result[0:6]
            return result
    except RequestException:
        return None

def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print
        path + ' 创建成功'
        return path
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False

def prase_page(url):
    try:
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'lxml')
            h1 = soup.find_all('article')
            # 获取图片标题
            title = BeautifulSoup(str(h1), 'lxml').get_text()
            title = str(title).split()[1:30]
            #获取图片链接
            patten = re.compile(r'.*?([a-zA-z]+://[^\s]*)"', re.S)
            img = patten.findall(str(h1))
            img_new = []
            for iten in img:
                if iten not in img_new:
                    img_new.append(iten)
            img_new = img_new[0:28]
            #下载图片
            path  = 'H:\渤海拾贝趣图\\' + title[0] + '\\'
            newpath = mkdir(path)
            for i in range(len(title)):
                time.sleep(1)
                download_img(newpath, title[i], img_new[i])

            return title, img_new
    except RequestException:
        return None

def download_img(path, title, img_url):
    if img_url[-3:] == 'jpg':
        pic = requests.get(img_url, headers=header, timeout=10)
        with open(path + title + '.jpg', 'wb') as f:
            print('正在下载', title)
            f.write(pic.content)
            f.close()
    else:
        pic = requests.get(img_url, headers=header)
        with open(path + title + '.gif', 'wb') as f:
            print('正在下载', title)
            f.write(pic.content)
            f.close()


def main():
    url = 'https://bh.sb/post/category/main/'
    r = get_page(url)
    for i in r:
        prase_page(i)


if __name__ == '__main__':
    main()