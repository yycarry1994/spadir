import requests
import time
from bs4 import BeautifulSoup
import pymysql
import lxml

class IpProxy():
    conn = pymysql.connect(host="127.0.0.1", user="root",password="123",database="testdb",charset="utf8")
    sql = conn.cursor()

    def __int__(self):

    def get_ip(self):
        '''
        从数据库里获取ip
        :return:(ip,port,speed,typle)
        无数据时返回None
        '''
        sql = '''select ip, port, speed, proxy_typle from proxy_ip order by rand() limit 1;'''
        self.sql.execute(sql)


    def prase_ip(self):
        '''
        爬取西刺免费代理ip池
        :return:无返回
        '''
        header = {
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
            "Host": "www.xicidaili.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        url = 'https://www.xicidaili.com/nn/'
        r_html = None
        for i in range(10):
            try:
                r_html = requests.get(url,headers=header,timeout = 10)
            except requests.exceptions.Timeout:
                print("请求超时，第%d次重新请求" % (i+1))
                r_html = requests.get(url, headers=header, timeout=10)
            if r_html.status_code == 200:
                break
        soup = BeautifulSoup(r_html,'lxml')




