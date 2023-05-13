# -*- coding: utf-8 -*-
import paramiko
import datetime
from currency import write_file
import os


class run_linux:
    def __init__(self, data_list):
        file_name, host, username, password, port = data_list.split("~")
        ssh = paramiko.SSHClient()  # 建立连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host, port=port, username=username, password=password, allow_agent=False,
                        look_for_keys=False, timeout=5)
            self.con_state = True  # 连接状态码
        except:
            self.con_state = False
            pass
        self.ssh = ssh
        self.file_name = "date/" + file_name + "+" + host + ".log"

    def run(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        write_file(self.file_name, stdout.read().decode("utf-8"))

    def __call__(self, cmd, *args, **kwargs):
        return self.run(cmd)


def run(data, cmd):
    linux_con = run_linux(data)
    if linux_con.con_state:  # 判断是否成功建立连接，若失败返回信息
        linux_con.run(cmd)
    else:
        error_date = "时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ",失败主机：" + \
                     data.split("~")[0] + "---" + data.split("~")[1] + "\n"
        print(error_date)
        write_file("error.log", error_date)
