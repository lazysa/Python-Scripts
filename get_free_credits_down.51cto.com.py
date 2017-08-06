#!/bin/env python
# -*- coding: utf-8 -*-
"""
# Run on Python3
# http://down.51cto.com/js/newjs/cent.js
# Used to:   Auto get (free|download)_credits(下载豆) on http://down.51cto.com
#------------------------------------------------------------------------------------------------
# Developer:    xu.chen
# Blog:         http://chenxu.info
# Email:        linuxjosery@gmail.com
# Created on:   2017/08/06
# Location:
# Execution:    get_free_credits_down.51cto.com.py
# Description:  每天自动在 "down51cto.com" 领取下载豆
# Revision History:
#
# Name             Date            Description
#------------------------------------------------------------------------------------------------
# xu.chen        2017/08/06      Initial Version
#------------------------------------------------------------------------------------------------
"""
import random,re
import sys,requests
from bs4 import BeautifulSoup

s = requests.Session()

def result (result_msg):
    result_file = "%s.txt" %(sys.argv[0])
    with open(result_file, 'wt') as f:
        print(result_msg, file=f)

def get_free_credits ():
    login_url = 'http://home.51cto.com/index'
    # If url is disabled, exit
    try:
        check_url = s.get(login_url)
        check_url.raise_for_status()
    except requests.RequestException as e:
        print(e)
        exit (2)

    login_data = {
	           '_csrf': 'WGNDcHpHa1kUIBoTDQ0bEjo2JR05M1g7NVUqHDQyOSkfUgoKPAUGBg==',
               'LoginForm[username]': 'chenxu123',
	           'LoginForm[password]': '123.com',
	           'LoginForm[rememberMe]': '1',
	           'login-button': '登 录'
    }

    headers = {
	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	        'Accept-Encoding': 'gzip, deflate',
	        'Accept-Language': 'zh-CN,zh;q=0.8',
	        'Cache-Control': 'max-age=0',
		    'Connection': 'keep-alive',
		    'Content-Length': '192',
		    'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'www51cto=32C34EDFA4D593B3EA03049F30BAE577qPsp; pgv_pvi=9748635648; pt_3f67dcc4=uid=IzbxxBoIZ1EkGRhucil2Kg&nid=0&vid=1W7CSqalwKGt29G/kMEUNQ&vn=4&pvn=1&sact=1469977501441&to_flag=0&pl=63dQEi/RdN/V6iAu21y-2g*pt*1469977501441; Hm_lvt_110fc9b2e1cae4d110b7959ee4f27e3b=1472612310; _ga=GA1.2.570890260.1462629768; _qddaz=QD.6xcx83.h0qse6.ix90zi2t; Cto_lvt_3d7ca8d8c01f7e7b50250ff1c15bdae3=1483026059; Cto_uid_3d7ca8d8c01f7e7b50250ff1c15bdae3=0; aliyungf_tc=AQAAAN/iB1o4qwkAdfih04Ammvoggm3y; _csrf=43964c02b53829f589a8e5ece024ea0fda823489a1d4418f01ada5c862c76a52a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22LCYcwJpKbUfmCt3bm6ilNuRpG1IzFBm_%22%3B%7D; _ourplusFirstTime=117-7-29-12-43-3; acw_tc=597c1255|0c00cf4fea4f46d028308aa9b6c14734; lastlogin=on; pub_visitedfid=221; pub_smile=1DD0D9; Hm_lvt_f77ea1ecd95cb2a1bc65cbcb3aaba7d4=1501304167; Hm_lpvt_f77ea1ecd95cb2a1bc65cbcb3aaba7d4=1501304171; pub_cookietime=0; PHPSESSID=lmaosbt7vt18jc6u3e5li11ef0; _ourplusReturnCount=41; _ourplusReturnTime=117-7-29-17-34-0; Cto_lvt_=1501303384,1501317581,1501318344,1501320839; Cto_lpvt_=1501320841; Cto_uid_=0; Hm_lvt_844390da7774b6a92b34d40f8e16f5ac=1501303384,1501317581,1501318344; Hm_lpvt_844390da7774b6a92b34d40f8e16f5ac=1501320841',
		    'Host': 'home.51cto.com',
		    'Origin': 'http://home.51cto.com',
		    'Referer': 'http://home.51cto.com/index?reback=http%253A%252F%252Fdown.51cto.com%252Fcredits',
		    'Upgrade-Insecure-Requests': '1',
		    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    # Login website
    r = s.post(login_url, data=login_data, headers=headers)
    credits_url = 'http://down.51cto.com/download.php?do=getfreecredits&t=%s' %(random.random())
    # send credits's request

    r = s.post(credits_url)
    result_tuple = ((r.text))
    # convert result to tuple
    cres_id = result_tuple[0]
    # get cres_id
    cres_total = result_tuple[2:5]
    #print(result_tuple)

    if cres_id == '0':
        result_msg = 'get download_credits failure! maybe login problem.'
        result(result_msg)
    elif cres_id == '1':
        result_msg = "You've already got download_credits today, Total: %s" %(cres_total)
        result(result_msg)
    else:
        result_msg = 'get 2 download_credits success!, Total: %s' %(cres_total)
        result(result_msg)
"""
    credits_url = 'http://down.51cto.com/credits'
    r = s.post(credits_url, data=login_data, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)

    result = soup.find_all(re.compile("class='channel0'"))
    print(result)
"""

# Call query_result() when this file is run as a script (not imported as a module)
if __name__ == '__main__':
    get_free_credits()
