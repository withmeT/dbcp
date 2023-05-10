# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/28 15:31
@Auth ： Tian Pengtao
@File ：currency.py
"""
#通用函数
import re
import os

#读文件函数
def read_file(file):
    date = []
    with open(file,"r+",encoding="utf-8") as f:
        for i in f.readlines():
            date.append(i.replace("\n",""))
    return date
#写入文件函数
def write_file(file,date):
    with open(file, "a+", encoding="utf-8") as f:
        f.write(date)

#判断文件是否存在
def file_exists(file):
    if os.path.exists(file) == True:
        return True
    else:
        return False

#判断格式是否正确
def check_in_date(date):
    Wrong_character = ["\\","/",":","*","?","<",">","|"]
    date = date.split("~")
    if len(date) != 5:
        print("参数个数不合规")
        return None
    #IP格式正则
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if any(substring in date[0] for substring in Wrong_character):
        print(date[0] + "---" + "名称包含不符合字符")
        return None
    if not compile_ip.match(date[1]):
        print(date[0] + "---" + "IP格式不满足要求")
        return None
    if (int(date[4]) <= 0) or (int(date[4])> 65535):
        print(date[0] + "---" + "端口号不符合要求，1~65535")
        return None
    return True