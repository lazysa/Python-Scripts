#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

import os
import csv
import gzip
import pyodbc

""" 解决 python2 编码转换问题，但副作用是 print 失效
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""

def main():
    n = 0
    con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'EC2AMAZ-DRM7L9D', database = 'master')
    cur = con.cursor()
    results = cur.execute(sqlstring)
    #columns = [desc[0] for desc in cur.description]

    os.mkdir(tb_name)
    os.chdir(tb_name)
    f=gzip.open('table.dat.gz', "wb")
    csv_w = csv.writer(f, lineterminator='\n')
    #csv_w.writerow(columns)
    for row in results:
        csv_w.writerow(row) 
        n += 1
    f.close()
    print("Total rows: {}".format(n))
    os.chdir(r'D:\table-new')
    return 
         

def dump0 (table):
    for i in range(len(table)):
        db_name = '[buy2016_2].[dbo].'
        global tb_name 
        tb_name = table[i]
        global sqlstring
        sqlstring = "SELECT FLOWNO,POSNO,ITEMNO,GID,QTY,PRICE,REALAMT,LSTUPDTIME,fildate,gdcode,dealtime FROM " + db_name + tb_name
        #print (db_name + tb_name)     
        main()
        #print (sqlstring)
        
def dump1 (table):
    for i in range(len(table)):
        db_name = '[buy2017].[dbo].'
        global tb_name 
        tb_name = table[i]
        global sqlstring
        sqlstring = "SELECT FLOWNO,POSNO,ITEMNO,GID,QTY,PRICE,REALAMT,'',fildate,gdcode,dealtime FROM " + db_name + tb_name
        #print (db_name + tb_name)     
        main()

def dump2 (table):
    for i in range(len(table)):
        db_name = '[buy20170525].[dbo].'
        global tb_name 
        tb_name = table[i]
        global sqlstring
        sqlstring = "SELECT FLOWNO,POSNO,ITEMNO,GID,QTY,PRICE,REALAMT,LSTUPDTIME,fildate,gdcode,'' FROM " + db_name + tb_name
        #print (db_name + tb_name)     
        main()


#dump0( table = ['[buy22016_10]', '[buy22016_11]', '[buy22016_12]'] )
#dump1( table = ['[buy2_201703]', '[buy2_20170322_31]', '[buy2_201704]', '[buy2_20170426_30]'] )
dump2( table = ['[buy22015_07]', '[buy22015_08]', '[buy22015_0901_0910]', '[buy22015_09011_0920]', '[buy22015_0921_0930]', '[buy22015_1001_1010]', '[buy22015_1011_1020]', '[buy22015_1021_1030]', '[buy22015_1101_1111]', '[buy22015_1111_1120]', '[buy22015_1121_1130]', '[buy22015_1201_1212]', '[buy22015_1212_1220]', '[buy22015_1221_1230]', '[buy22015_1-6]'] )
