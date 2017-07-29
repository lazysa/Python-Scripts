#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auto sing in on http://data.jobbole.com
import sys,requests,json

def sign_in ():
    login_url = 'http://date.jobbole.com/wp-login.php'
    result_file = "%s.txt" %(sys.argv[0])
    s = requests.Session()
    # If url is disabled, exit
    try:
        check_url = s.get(login_url)
        check_url.raise_for_status()
    except requests.RequestException as e:
        print(e)
        exit (2)

    login_data = {'log': 'Lazysa', 'pwd': '123.com'}
    headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'date.jobbole.com',
            'Origin': 'http://date.jobbole.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
    }

    r = s.post(login_url, data=login_data, headers=headers)
    url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
    data = {'action': 'get_login_point'}

    r = s.post(url, data=data, headers=headers)
    respon_dict = json.loads(r.text)
    result = respon_dict['jb_result']

    if result == 0:
        result_f = '今天已签到，现有积分:%s. 一大波MM正在路上^~^' %(respon_dict['user_points'])
        with open(result_file, 'wt') as f:
            print(result_f, file=f)
    elif result == -1:
        pass
        """with open(result_file, 'wt') as f:
            print(respon_dict['jb_msg'], file=f)
		"""

# Call query_result() when this file is run as a script (not imported as a module)
if __name__ == '__main__':
    sign_in()
