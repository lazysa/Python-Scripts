#!/bin/env python
# -*- coding: utf-8 -*-
"""
# Run on Python3
# Used to:   MSSQL's table -> .dat(CSV)
#------------------------------------------------------------------------------------------------
# Developer:    xu.chen
# Blog:         http://chenxu.info
# Email:        linuxjosery@gmail.com
# Created on:   2017/08/06
# Location:
# Execution:    sql_dump_dat.py
# Description:  将 MSSQL中的表导出为.dat文件（CSV格式）
# Revision History:
#
# Name             Date            Description
#------------------------------------------------------------------------------------------------
# xu.chen        2017/08/06      Initial Version
#------------------------------------------------------------------------------------------------
"""

import os,time,random
#import getopt,io
import csv
import gzip
import pyodbc
import multiprocessing

""" 解决 python2 编码转换问题 """
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def usage():
    """
Dump SQL Server Table to dat file(csv format).

Usage: sql-dump-dat.py  [-h|--help]
Description
            -d,--database.
            -m,--mode  full dump or dump TOP (100).
            -h,--help    Display help information.

for example:
    python sql-dump-dat.py -d  buy2016 buy2016_2 mini
    python sql-dump-dat.py -d  buy2016 buy2016_2 full
"""

def dump(table, sqlstring, mode):
    #basedir = 'D:\table-new'
    n = 0
    con = pyodbc.connect('Trusted_Connection=yes', driver = '{SQL Server}',server = 'EC2AMAZ-DRM7L9D', database = 'master')
    cur = con.cursor()
    results = cur.execute(sqlstring)
    ## insssert fields into first line
    #columns = [desc[0] for desc in cur.description]

    """
    os.mkdir(table)
    #f = gzip.open('table.dat.gz', "wb")
    #csv_w = csv.writer(f, lineterminator='\n')
    #csv_w.writerow(columns)
    """
    # python3
    # with open(table + '.dat', 'w', newline='', encoding='utf-8') as f:
    #


    with open(table + mode + '.dat', 'wb') as f:
        csv_w = csv.writer(f, lineterminator='\n')
        ## insert fields into first line
        #csv_w.writerow(columns)
        for row in results:
            csv_w.writerow(row)
            n += 1
    #f.close()
        print("Table: {0}    Total rows: {1}".format(table, n))
    os.chdir(r'D:\table-new')
    return


def string(database, table, mode):
    if mode in ['mini', 'MINI']:
        top = 'TOP (100)'
    elif mode in ['full', 'FULL']:
        top = ''

    """for i in range(len(table)):
        #global tb
        tb = table[i]
    """
    sqlstring0 = "SELECT %s FLOWNO,POSNO,ITEMNO,GID,QTY,PRICE,REALAMT,LSTUPDTIME,fildate,gdcode,'' FROM [%s].[dbo].[%s]"  %(top,database,table)

    # Make different sqlstring
    if table in ['buy2015_01', 'buy2015_02', 'buy2015_03', 'buy2015_04', 'buy2015_05', 'buy2015_06']:
        sqlstring = sqlstring0

    #print(sqlstring)
    dump(table, sqlstring, mode)

"""
         # Make different sqlstring
        if database in ['buy2016', 'buy2016_2']:
            sqlstring = sqlstring0
        elif database in [ 'buy2017']:
            if table in ['buy2_201703', 'buy2_20170322_31', 'buy2_201704', 'buy2_20170426_30']:
                sqlstring = sqlstring1
            else:
                sqlstring = sqlstring0
        elif database in ['buy20170525']:
            if table in ['buy22016_01', 'buy22016_02']:
                sqlstring = sqlstring0
            else:
                sqlstring = sqlstring2

        #exec()
"""


def tablename (database):
    if database == 'buy2015':
        global table
        table = ['buy2015_01', 'buy2015_02', 'buy2015_03', 'buy2015_04', 'buy2015_05', 'buy2015_06']
    else:
        usage()


def worker0():
    #print ("worker0")
    database = sys.argv[1]
    tablename(database)
    string(database, table[0], sys.argv[2])
    #print ("end worker0")

def worker1():
    #print ("worker1")
    database = sys.argv[1]
    tablename(database)
    string(database, table[1], sys.argv[2])
    #time.sleep (200)
    #print ("end worker1")

def worker2():
    #print ("worker1")
    database = sys.argv[1]
    tablename(database)
    string(database, table[2], sys.argv[2])
    #time.sleep (200)
    #print ("end worker1")

def worker3():
    #print ("worker1")
    database = sys.argv[1]
    tablename(database)
    string(database, table[3], sys.argv[2])
    #time.sleep (200)
    #print ("end worker1")

def worker4():
    #print ("worker1")
    database = sys.argv[1]
    tablename(database)
    string(database, table[4], sys.argv[2])
    #time.sleep (200)
    #print ("end worker1")

def worker5():
    #print ("worker1")
    database = sys.argv[1]
    tablename(database)
    string(database, table[5], sys.argv[2])
    #time.sleep (200)
    #print ("end worker1")


if __name__ == '__main__':
    #q = Queue()
    pw0 = multiprocessing.Process(target=worker0)
    pw1 = multiprocessing.Process(target=worker1)
    pw2 = multiprocessing.Process(target=worker2)
    pw3 = multiprocessing.Process(target=worker3)
    pw4 = multiprocessing.Process(target=worker4)
    pw5 = multiprocessing.Process(target=worker5)


    pw0.start()
    #pw0.join()
    pw1.start()
    #pw1.join()
    pw2.start()
    pw3.start()

    pw4.start()
    pw5.start()


"""
    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print ("END!!!!!!!!!!!!!!!!!")
"""


