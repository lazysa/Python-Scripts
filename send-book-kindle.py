#!/bin/env python 
# -*- coding: utf-8 -*-
""" Usend to download mini-book on infoq 
    And send it to my Kindle 
"""

import urllib
import urllib2,StringIO
import requests,re,os
import datetime
# Send e-mail modules 
#pip install mailer
from mailer import Mailer
from mailer import Message

os.chdir(r'E:\main\infoq-architect')
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
url_half01 = 'http://www.infoq.com/cn/minibooks/download/architect-'
url = [url_half01, now_year, last_month, '?bookFormat=mobi']
url = ''.join(url)
"""
url = 'http://www.infoq.com/cn/minibooks/download/architect-%s%s?bookFormat=mobi' %(now_year, last_month))

headers = { #伪装为浏览器抓取
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

#r = requests.get(url, stream=True)
r = requests.get(url, auth=('chenxuwq@163.com', '@Lan13826358458'))

if r.status_code == 200:
   # request = urllib2.Request(url,headers=headers)
    response = urllib.urlopen(url)
 #   response = StringIO(response.read())
    with open("architect.mobi","wb") as f:
        f.write(response.read())
    """#with open("architect.mobi", "wb") as code:
        #code.write(r.content)

   # with open(url, "wb") as code:
        #code.write(date)"""

