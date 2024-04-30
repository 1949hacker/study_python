import paramiko,re
from os import system as sys

def flashBin(hostname, port, username, password, local_file, remote_path):
    try:
        # 创建SSH客户端
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh_client.connect(hostname=hostname, port=port, username=username,
                           password=password)

        # 创建SCP客户端
        scp_client = ssh_client.open_sftp()

        # 上传文件
        scp_client.put(local_file, remote_path)
        print(f"文件 {local_file} 已上传到 {remote_path}")

        # 核验nvme信息
        command_check = "nvme id-ctrl /dev/nvme0n1 | grep fr"
        stdin, stdout, stderr = ssh_client.exec_command(command_check)
        match = re.search(r'fr\s*:\s*(\w+)', stdout.read().decode())
        print("刷写前固件版本:"+match.group(1))

        # 开始刷写
        command_download = "nvme fw-download /dev/nvme0n1 -f firmware"
        stdin, stdout, stderr = ssh_client.exec_command(command_download)
        print(stdout.read().decode())
        command_flash = "nvme fw-commit /dev/nvme0n1 -s 1 -a 3"
        stdin, stdout, stderr = ssh_client.exec_command(command_flash)
        print(stdout.read().decode())

        # 检查刷写结果
        command_check = "nvme id-ctrl /dev/nvme0n1 | grep fr"
        stdin, stdout, stderr = ssh_client.exec_command(command_check)
        match = re.search(r'fr\s*:\s*(\w+)', stdout.read().decode())
        print("刷写完成!固件版本:" + match.group(1))

        # 关闭SCP客户端和SSH客户端
        scp_client.close()
        ssh_client.close()
    except Exception as e:
        print(f"操作失败:{e}")

sys("@echo off")
sys("color 0a")
sys("title 昱格BIOS刷写工具")
print("欢迎使用昱格——海康威视NVMe 128G "
      "SSD固件刷写工具，刷写之前需要准备好支持ssh连接和nvme命令的Linux系统\n推荐使用YGENAS开启ssh服务并允许root"
      "使用密码登陆!")
hostname = input("目标IP:")

port = input("端口默认为22，无需修改则直接按Enter，否则请输入后再按Enter:")
if port == "" :
    port = 22

username = "root"
password = input("密码默认为Yge123456，无需修改则直接按Enter，否则请输入后再按Enter:")
if password == "" :
    password = "Yge123456"

local_file = input("默认刷写的是海康威视128G "
                 "SSD的固件，如需刷写其他容量的固件，请将其重命名为firmware后放到本工具所在目录，注意是firmware"
                 "，没有后缀名！\n执行默认刷写请直接按Enter，或者将默认firmware替换后按Enter:")
if local_file == "" :
        local_file = "firmware"
remote_path = "/root/firmware"

flashBin(hostname, port, username, password, local_file, remote_path)

print("按ESC退出程序.")
sys('pause>nul')
