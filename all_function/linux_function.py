# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/28 16:29
@Auth ： Tian Pengtao
@File ：linux_function.py
"""
import paramiko
import datetime
import time
from currency import write_file
class run_linux:
    def __init__(self,date_list):
        t1 = time.time()
        file_name, host, username, password, port = date_list.split("~")
        ssh = paramiko.SSHClient()  # 建立连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host, port=port, username=username, password=password, allow_agent=False,
            look_for_keys=False, timeout=3)
            self.con_state = True                     #连接状态码
        except:
            self.con_state = False
            pass
        self.ssh = ssh
        self.file_name = "date/" + file_name + "+" + host + ".log"
        t2 = time.time()
        print(t2-t1)
    def run(self,cmd):
        if self.con_state == True :
            for i in cmd:
                stdin, stdout, stderr = self.ssh.exec_command(i)
                write_file(self.file_name,stdout.read().decode("utf-8"))
        else :
            error_date = "时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ",失败主机：" + i.split("~")[0] + "---" + i.split("~")[1] + "\n"
            print(error_date)
            write_file("error.log",error_date)
    def __call__(self, cmd, *args, **kwargs):
        return self.run(cmd)

