#coding = utf-8

import re
import requests

url = 'https://www.ichunqiu.com/courses'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
r = requests.get(url=url,headers = headers,verify = False)

names = re.findall('<div class="coursename" title="(.*)" onclick',r.content)
for name in names:
    print name
