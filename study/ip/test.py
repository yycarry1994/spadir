import requests
headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTZjNDNmNjgzZWY5OWQ4ZWRmNTA5MzU3YWJiOGJlYWMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVBsU3h6aU0xa25KWlZXZE5qZ0tGd21xYkJtc3J0K2w0YlEwdUhlNjFBN009BjsARg%3D%3D--abe7f4154a205b8515bfb204e3fe924006ae1d68",
            "Host": "www.xicidaili.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
        }

url = 'http://www.xicidaili.com/nn/'
r_html = None
for i in range(2):
    try:
        r_html = requests.get(url, headers=headers, timeout=10)
    except requests.exceptions.Timeout:
        print("请求超时，第%d次重新请求" % (i+1))
        r_html = requests.get(url, headers=headers, timeout=10)
    if r_html.status_code == 200:
        break
print(r_html.text)