#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys

import datetime

import openpyxl
from openpyxl.styles import Alignment
from openpyxl.styles import Font

import pymongo,ssl
import re





# get mongodb data lines
# db_host              mongodb地址
# db_port              mongodb端口
# db_auth_name         mongodb的账号
# db_auth_password     mongodb的密码
# db_auth_db           mongodb授权库
# db_name              mongodb数据库
# 返回（mongodb连接，库下所有的表）
def read_mongodb_data(db_host, db_port, db_auth_name, db_auth_password, db_auth, db_name):
    client = pymongo.MongoClient(db_host, db_port,ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
    db_auth = client[db_auth]
    db_auth.authenticate(name=db_auth_name, password=db_auth_password,mechanism="SCRAM-SHA-1") 
    db = client[db_name]
    collections = db.collection_names(include_system_collections=False)
    return (db, collections)  
#for i in read_mongodb_data("jscert.finsec.org", 27017, "testbuf", "testtestbuf", "userdetail", "userdetail"):
#    print(i)





#read xlsx data lines
# xlsx_name            被读取xlsx表名
# *cols                变长参数（需要读取的列）
# 返回读取到的xlsx数据，以列为单位
def read_xlsx_data(xlsx_name, *cols):
 xl = openpyxl.load_workbook(xlsx_name)
 wb = xl.active
 datas = {}
 for col in cols:
  lines = []
  for line in wb[col]:
   lines.append(line.value)
  datas[col] = lines
 return datas 
#data_lines = read_xlsx_data("every_day.xlsx","A","B","C")
#print(data_lines["A"])
#print(data_lines["B"])
#print(data_lines["C"])





#write data to xlsx
# xlsx_name            写入xlsx表名
# data_lines           二维数组
def write_data_to_xlsx(xlsx_name, data_lines):
 wb = openpyxl.Workbook()
 sheet = wb.active
 l = 0
 AZ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "v", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
 for cols in data_lines:
  j = 1
  for col in cols:
   sheet["%s%d"%(AZ[l],j)] = col
   j += 1   
  l += 1
 wb.save('%s'%xlsx_name)
#write_data_to_xlsx("data.xlsx",[data_lines["A"], data_lines["B"]])






# str time to date time
def time_str_to_date(time_str):
 return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

def timestamp_to_date(timestamp):
 return datetime.datetime.fromtimestamp(timestamp)













