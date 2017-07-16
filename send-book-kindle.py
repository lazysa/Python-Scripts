#!/bin/env python 
# -*- coding: utf-8 -*-
""" Usend to download mini-book on infoq 
    And send it to my Kindle 
"""

import urllib
#import urllib2,StringIO
import requests,re,os
import datetime
#from io import BytesIO
# Send e-mail modules 
#pip install mailer
from mailer import Mailer
from mailer import Message


os.chdir(r'D:\infoq-architect')

def getUrl(): 
    # Get date Year and Month 
    now = datetime.datetime.now()
    last_month = now.month - 1 

    # Int to String 
    now_year = str(now.year)
    last_month = str(last_month)    

    # Single month to Doble month 
    if len(str(last_month)) == 1:
        last_month = str(0) + last_month

    # Get download URL
    """
    url_half01 = 'https://www.infoq.com/cn/minibooks/download/architect-'
    url = [url_half01, now_year, last_month, '?bookFormat=pdf']
    url = ''.join(url)
    """  
    global url 
    url = 'https://www.infoq.com/cn/minibooks/download/architect-%s%s?bookFormat=pdf' %(now_year, last_month)
    global headers
    headers = { #伪装为浏览器抓取
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

     
    #r = requests.get(url, stream=True)


getUrl()

s = requests.Session()
login_data = {'Email': 'chenxuwq@163.com', 'Password': '123.com',}

# post 数据实现登录
r = s.post('https://www.infoq.com', login_data)
r = 



"""
# debug 
print (url)
print (headers)
"""
"""
#with requests.Session() as c:


r = requests.Session()
r.auth = ('chenxuwq@163.com', '123.com')
r.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'})
#if r.status_code == 200:
with requests.Session("now_year-last_month.pdf", 'wb') as f:
    f.write(r.content)


r = requests.get(url, auth=('chenxuwq@163.com', '123.com'))

if r.status_code == 200:
    r.content
"""

"""
   # request = urllib2.Request(url,headers=headers)
    response = urllib.request.urlopen(url)
 #   response = StringIO(response.read())
    with open("architect.mobi","wb") as f:
        f.write(response.read())
    #with open("architect.mobi", "wb") as code:
        #code.write(r.content)

   # with open(url, "wb") as code:
        #code.write(date)
"""
        