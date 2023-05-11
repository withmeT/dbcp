# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/28 16:29
@Auth ： Tian Pengtao
@File ：linux_function.py
"""
import paramiko
from currency import write_file


class run_linux:
    def __init__(self, data_list):
        file_name, host, username, password, port = data_list.split("~")
        ssh = paramiko.SSHClient()  # 建立连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=host, port=port, username=username, password=password, allow_agent=False,
                        look_for_keys=False, timeout=3)
            self.con_state = True  # 连接状态码
        except:
            self.con_state = False
            pass
        self.ssh = ssh
        self.file_name = "date/" + file_name + "+" + host + ".log"

    def run(self, cmd):
        for i in cmd:
            stdin, stdout, stderr = self.ssh.exec_command(i)
            write_file(self.file_name, stdout.read().decode("utf-8"))

    def __call__(self, cmd, *args, **kwargs):
        return self.run(cmd)
