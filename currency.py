# 通用函数
import re
import os


# 读文件函数
def read_file(file):
    data = []
    with open(file, "r+", encoding="utf-8") as f:
        for i in f.readlines():
            data.append(i.replace("\n", ""))
    return data


# 写入文件函数
def write_file(file, data):
    with open(file, "a+", encoding="utf-8") as f:
        f.write(data)


# 判断文件是否存在
def file_exists(file):
    if os.path.exists(file) == True:
        return True
    else:
        return False


# 判断格式是否正确
def check_in_data(data):
    Wrong_character = ["\\", "/", ":", "*", "?", "<", ">", "|"]
    data = data.split("~")
    if len(data) != 5:
        print("参数个数不合规")
        return None
    # IP格式正则
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if any(substring in data[0] for substring in Wrong_character):
        print(data[0] + "---" + "名称包含不符合字符")
        return None
    if not compile_ip.match(data[1]):
        print(data[0] + "---" + "IP格式不满足要求")
        return None
    if (int(data[4]) <= 0) or (int(data[4]) > 65535):
        print(data[0] + "---" + "端口号不符合要求，1~65535")
        return None
    return True
