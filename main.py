import argparse

from all_function.threads import *
from all_function.linux_function import run_linux
import yaml

if not os.path.exists("date"):  # 判断是否存在存储采集结果的目录
    os.makedirs("date")

with open("default.yaml", "r", encoding="utf8")as f:  # 读取本地默认参数
    cli_yaml = yaml.safe_load(f)


def cli():  # 设置参数
    parser = argparse.ArgumentParser(description='等保测评工具')
    subparsers = parser.add_subparsers(dest="command")
    subparser1 = subparsers.add_parser('linux', help='linux help')
    subparser1.add_argument('--host', dest='host', help='单主机采集（以”设备名~IP地址~用户名~密码~端口“）')
    subparser1.add_argument('--hosts', dest='hosts', help='多主机采集(default ./linux.txt)',
                            default=cli_yaml.get("linux-hosts"))
    subparser1.add_argument('--common', dest='comm', help='自定义命令采集(以分号进行分割)')
    subparser2 = subparsers.add_parser('mysql', help='mysql help')
    subparser2.set_defaults()
    return parser.parse_args()


if __name__ == '__main__':  # 主函数
    args = cli()
    if args.command == 'linux':  # linux模式
        with open("cmd.yaml", "r", encoding="utf8")as f:
            cmd = yaml.safe_load(f).get("linux_cmd")
        if args.comm:  # 判断是否自定义命令
            cmd = args.comm
        if args.host:  # 主机类型为单主机采集
            if check_in_data(args.host):
                run_linux(args.host).run(cmd=cmd)
        elif args.hosts:  # 主机类型为多主机采集
            linux_threads_pool(args.hosts, cmd=cmd)
