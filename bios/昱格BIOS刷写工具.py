from os import system as sys
import random
import string
from datetime import datetime

def generate_random_string():
    # 获取当前时间
    current_time = datetime.now()
    # 将时间戳转换为字符串并去掉分隔符
    timestamp_str = str(current_time.timestamp()).replace('.', '')

    # 生成一个随机字符串
    random_chars = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))

    # 结合当前时间戳字符串和随机字符串
    final_string = timestamp_str[-4:] + random_chars

    return final_string

sys("@echo off")
sys("color 0a")
sys("title 昱格BIOS刷写工具")

print("欢迎使用昱格BIOS刷写工具\n在开始之前,需要设定几个参数的值.\nBP 产品的名称,命名规则为YGENAS-桌面式V/机架式R-盘位数量（Hx）-型号（ A-Z）\nBV 产品的版本,如V1.0\nBS 产品的序列号,使用SNCreator生成.")

check = 'n'
while check == 'n':
    match check:
        case 'y':
            break
        case 'n':
            bm = input("请输入BM参数的值:")
            bp = input("请输入BP参数的值:")
            bv = input("请输入BV参数的值:")
            bs = generate_random_string()
            print('自动生成的序列号是:%s'%bs)
            check = input("您输入的值分别是:\nBP: %s\nBV: %s\nBS: %s\n请核对!(y/n)" % (bp,bv,bs))

print("接下来将开始BIOS刷入,请等待...")

command = 'AMIDEWINx64.EXE /BM "%s" /BP "%s" /BV "%s" /BS "%s"' % (bm,bp,bv,bs)
system_command = 'AMIDEWINx64.EXE /SM "%s" /SP "%s" /SV "%s" /SS "%s"' % (bm,bp,bv,bs)
print(command)
sys(command)

print("BIOS刷入完毕,请检查是否刷入正确:")
sys('AMIDEWINx64.EXE /BM /BP /BV /BS')
print("按ESC退出程序.")
sys('pause>nul')