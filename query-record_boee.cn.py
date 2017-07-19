#!/bin/env python 
# -*- coding: UTF-8 -*-
#  Results study record from 'wwww.boee.cn'

import os,sys,requests
from bs4 import BeautifulSoup

def usage():
    print(
    """
Usage: query-record_boee.cn.py {now|history} {exam_number}
    Description 
    {now|history}   # query mode
    {exam_number}   # need query's exam_number

for example:
    # query history exam result, use python3 run 
    # 输入你的学号，查询历史成绩
    py -3 query-record_boee.cn.py history exam_number(学号)
    python query-record_boee.cn.py history exam_number(学号)
    """
    ) 

def query_result(record_cycle, exam_number): 
    rd_now_url = 'http://www.boee.cn/jtbm/cjc.aspx'
    rd_history_url = 'http://www.boee.cn/jtbm/lscjcx.aspx'
    result_file = "query-record_%s.html" %(record_cycle) 

    s = requests.Session()
    now_data = {
                 'ctl00$ScriptManager1': 'ctl00$cph_Main$UpdatePanel1|ctl00$cph_Main$txtZKZ',
                'ctl00$cph_Main$txtZKZ': exam_number,
                '__EVENTTARGET': 'ctl00$cph_Main$txtZKZ',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VIEWSTATE': '/wEPDwULLTE5NzQwMjMyMjkPZBYCZg9kFgICAw9kFggCAw9kFgICAQ8WAh4EVGV4dAUSICZndDsg5oiQ57up5p+l6K+iZAIFDxYCHgdWaXNpYmxlZxYCAgEPFgIeCWlubmVyaHRtbAWdAjxsaSBzdHlsZT0id2lkdGg6MjMwcHgiPjxhIGhyZWY9Imh0dHA6Ly93d3cuc2hmdGp5LmNvbS8iIHRhcmdldD0iX2JsYW5rIiBvbkNsaWNrPUFEQ291bnRlcigxMzApID4NCjxpbWcgc3JjPSJodHRwOi8vd3d3LmJvZWUuY24vanRibS9hZHMvZnV0b25nLmpwZyIgYWx0PSLlpI3lkIzmlZnogrIiIC8+DQo8L2E+DQo8L2xpPjxsaSBzdHlsZT0id2lkdGg6MjMwcHgiPjwvbGk+PGxpIHN0eWxlPSJ3aWR0aDoyMzBweCI+PC9saT48bGkgY2xhc3M9Imxhc3RhZCIgc3R5bGU9IndpZHRoOjIzMHB4Ij48L2xpPmQCBw9kFgICAQ8WAh8ABYcCPGxpIGNsYXNzPSJzZWxlY3RlZCI+PGEgaHJlZj0iaHR0cDovL3d3dy5ib2VlLmNuL2p0Ym0vY2pjeC5hc3B4Ij7miJDnu6nmn6Xor6I8L2E+PC9saT48bGk+PGEgaHJlZj0iaHR0cDovL3d3dy5ib2VlLmNuL0pUQk0vWktRS0NYLkFTUFgiPueJoeS4ueiHquiAg+WNoeWItuWNoeaDheWGteafpeivoiA8L2E+PC9saT48bGk+PGEgaHJlZj0iaHR0cDovL3d3dy5ib2VlLmNuL2p0Ym0vbHNjamN4LmFzcHgiPuiHquiAg+WOhuWPsuaIkOe7qeafpeivoiA8L2E+PC9saT5kAgkPZBYCAgEPZBYEAgEPFgIfAgUXMjAxN+W5tDTmnIjmiJDnu6nmn6Xor6JkAgMPZBYCZg9kFgQCAQ8PFgIfAWdkFgICAQ8PFgIfAGVkZAIDDw8WAh8BaGQWBgIBDw8WBB8AZR8BaGRkAgMPDxYCHwFnZBYGAgEPDxYCHwAFDDMxNTAxMTIzMDQzNWRkAgMPDxYCHwAFBumZiOaXrWRkAgUPFgIfAgXbBDxUQUJMRSBjZWxsU3BhY2luZz0nMScgY2VsbFBhZGRpbmc9JzEnIHdpZHRoPSc2NDAnIGJvcmRlcj0nMSc+PFRSPjxURCBzdHlsZT0nV0lEVEg6IDg2cHgnPjxQIGFsaWduPSdjZW50ZXInPjxGT05UIGZhY2U9J+Wui+S9kyc+PFNUUk9ORz7or77nqIvku6PnoIE8L1NUUk9ORz48L0ZPTlQ+PC9QPjwvVEQ+PFREIHN0eWxlPSdXSURUSDo0NjBweCc+PFAgYWxpZ249J2NlbnRlcic+PEZPTlQgZmFjZT0n5a6L5L2TJz48U1RST05HPuivvueoi+WQjeensDwvU1RST05HPjwvRk9OVD48L1A+PC9URD48VEQgc3R5bGU9J1dJRFRIOiA4NnB4Jz48UCBhbGlnbj0nY2VudGVyJz48Rk9OVCBmYWNlPSflrovkvZMnPjxTVFJPTkc+5oiQ57upPC9TVFJPTkc+PC9GT05UPjwvUD48L1REPjwvVFI+PFRSPjxURD48UCBhbGlnbj0nY2VudGVyJz4wMDA0MTwvUD48L1REPjxURD48UD7ln7rnoYDkvJrorqHlraY8L1A+PC9URD48VEQ+PFAgYWxpZ249J2NlbnRlcic+NzA8L1A+PC9URD48L1RSPjx0cj48dGQgY29sc3Bhbj0nMycgc3R5bGU9J3RleHQtYWxpZ246bGVmdDsnPkhhc2g6REUzOUI4NDFEMTcyOTI4NUJDQ0NDODE0RTQ5MjNFRENCQzNERERFMDwvdGQ+PC90cj48L1RBQkxFPmQCBw8WAh8CBbECPFA+PEZPTlQgZmFjZT0n5a6L5L2TJyBjb2xvcj0nI2ZmMDAwMCc+5pys5LiT5Lia5LiL5qyh5byA6ICD6K++56iL5LiO6LSt5Lmw5pWZ5p2Q6K+35rOo5oSP5LiL6Z2iPC9GT05UPjwvUD48aWZyYW1lIHdpZHRoPScxMDAlJyBmcmFtZUJvcmRlcj15ZXMgd2lkdGg9JzEwMCUnIGhlaWdodD0nMTAwJScgbWFyZ2lud2lkdGg9MSBtYXJnaW5oZWlnaHQ9MSBuYW1lPSdhYWEnIHNyYz0naHR0cDovL3d3dy5ib2VlLmNuL25ld3MvQXJ0aWNsZS8yMDA2LzIwMDYwNy8yMDA2LTA3LTI2LzIwMDYwNzI2MTExNzQ5Xzg1LnNodG1sJz48L2lmcmFtZT5kZPpGiqbGc1oa0CIL4JxO7HZZt5Tz',
                '__VIEWSTATEGENERATOR': 'B7F06CD5',
                '__EVENTVALIDATION': '/wEWAwLdj7U9ApDc0uYIAv36+7ALJz78th1QF55eroyMXCoP8ba3TLI=',
                '__ASYNCPOST': 'true'
    }     

    history_data = {
                     'ctl00$ScriptManager1': 'ctl00$cph_Main$UpdatePanel1|ctl00$cph_Main$btnSearch', 
                     '__EVENTTARGET': '',
                     '__EVENTARGUMENT': '',
                     '__VIEWSTATE': '/wEPDwULLTE0ODEzOTYxMDEPZBYCZg9kFgICAw9kFgQCAw9kFgICAQ8WAh4EVGV4dAUfICZndDsg6Ieq6ICD5Y6G5Y+y5oiQ57up5p+l6K+iIGQCBw9kFgICAQ8WAh8ABYcCPGxpPjxhIGhyZWY9Imh0dHA6Ly93d3cuYm9lZS5jbi9qdGJtL2NqY3guYXNweCI+5oiQ57up5p+l6K+iPC9hPjwvbGk+PGxpPjxhIGhyZWY9Imh0dHA6Ly93d3cuYm9lZS5jbi9KVEJNL1pLUUtDWC5BU1BYIj7niaHkuLnoh6rogIPljaHliLbljaHmg4XlhrXmn6Xor6IgPC9hPjwvbGk+PGxpIGNsYXNzPSJzZWxlY3RlZCI+PGEgaHJlZj0iaHR0cDovL3d3dy5ib2VlLmNuL2p0Ym0vbHNjamN4LmFzcHgiPuiHquiAg+WOhuWPsuaIkOe7qeafpeivoiA8L2E+PC9saT5kGAEFFWN0bDAwJGNwaF9NYWluJGd2SW5mbw9nZHbrXfwuXphi38XevLpt98j9ZSwB',
                     '__VIEWSTATEGENERATOR': '7AC18158',
                     '__EVENTVALIDATION': '/wEWAwLStuyJCwKQ3NLmCAL9+vuwC3pGZ4WamjhHqRkePE2khQNa+1vX',
                     'ctl00$cph_Main$txtZKZ': exam_number,
                     '__ASYNCPOST': 'true',
                     'ctl00$cph_Main$btnSearch': '查询'
    }     

    if record_cycle == 'now':
        post_data = now_data
        record_url = rd_now_url
    else:
        post_data = history_data
        record_url = rd_history_url

    # If Not in the query time, exit  
#    try:
#        s.get(record_url)
#    except HTTPError as e:
#        print(e)
#        exit(2)
#
    check = s.get(record_url)
    if check.status_code != 200:
        exit (2) 

   # Define record headers 
    rd_headers = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cache-Control': 'no-cache',
                'Content-Length': '917',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': 'www.boee.cn',
                'Origin': 'http://www.boee.cn',
                'Proxy-Connection': 'keep-alive',
                'Referer': record_url,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                'X-MicrosoftAjax': 'Delta=true'
    }           

    r = s.post(record_url, data=post_data, headers=rd_headers)
    

    # Transformation output results
    soup = BeautifulSoup(r.text, 'html.parser')

    if record_cycle == 'now':
        result = soup.div.prettify()
        with open(result_file, 'wt') as f:
            print (result, file=f)
    else:
        result0 = soup.findAll(id='ctl00_cph_Main_Panel1')
        result1 = soup.findAll(id='ctl00_cph_Main_dvSucc')
        with open(result_file, 'w+') as f:
            print (result0, file=f)
            print (result1, file=f)
       
# Call query_result() when this file is run as a script (not imported as a module)
if __name__ == '__main__':
        query_result (record_cycle=sys.argv[1], exam_number=sys.argv[2]);
