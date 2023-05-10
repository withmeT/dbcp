# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/1 23:14
@Auth ： Tian Pengtao
@File ：threads.py
"""
#linux线程池

from concurrent.futures import ThreadPoolExecutor
import datetime
import time
from all_function.linux_function import run_linux
from currency import *

def start_threads(date,cmd):
    run_linux(date).run(cmd=cmd)

def linux_threads_pool(file_name,cmd):
    if file_exists(file_name):
        new_date = []
        for i in read_file(file_name):  # 获取资产内容，并进行采集
            new_date.append(i)
        pool_num = len(new_date)
        pool = ThreadPoolExecutor(max_workers=pool_num)
        for i in new_date:  # 获取资产内容，并进行采集
            pool.submit(lambda cxp:start_threads(*cxp).run,(i,cmd))
        time.sleep(1)  # 不加延迟，会导致线程结果无法返回
    else:
        write_file("linux.txt", "名称~IP地址~用户名~密码~端口")
        print("文件不存在，以创建文件linux.txt，先补全信息吧")