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

def linux_threads_pool(file_name,cmd):
    if file_exists(file_name):
        pool_num = len(read_file(file_name))
        pool = ThreadPoolExecutor(max_workers=pool_num)
        for i in read_file(file_name):  # 获取资产内容，并进行采集
            if check_in_date(i):
                # pool.submit(lambda cxp:run(*cxp),(i ,cmd))
                linux_con = run_linux(i)
                if linux_con.con_state == True:  # 判断是否成功建立连接，若失败返回信息
                    pool.submit(linux_con.run, cmd)
                else:
                    error_date = "时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ",失败主机：" + i.split("~")[0] + "---" + i.split("~")[1] + "\n"
                    print(error_date)
                    write_file("error.log",error_date)
        time.sleep(1)  # 不加延迟，会导致线程结果无法返回
    else:
        write_file("linux.txt", "名称~IP地址~用户名~密码~端口")
        print("文件不存在，以创建文件linux.txt，先补全信息吧")