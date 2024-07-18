from os import system as sys
import random
import string
import re
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

print("欢迎使用昱格BIOS刷写工具\n产品的命名规则为YGENAS-桌面式V/机架式R-盘位数量（Hx）-型号（默认A,"
      "特殊型号会告知）和版本（默认V1.0，特殊版本会告知）\n12盘位标品NAS示例：YGENAS-R-H12-A版本V1.0")

check = 'n'
while check == 'n':
    match check:
        case 'y':
            break
        case 'n':
            bp = input("请输入产品名称（如YGENAS-R-H12-A）:")
            bv = input("请输入产品版本（默认V1.0）:")
            # [^-]匹配非-字符，+连续匹配，-包含-到匹配结果中，[^-]+-，连续匹配非-de字符并将-包含到结果中，如：YGENAS-
            # [^-]+-[^-]+-[^-]+，连续匹配2组符合*****-格式的和1组****格式的字符，也就是 YGENAS- R- H12~
            # .group(1)，.做为语法结构，表示调用re的match方法输出的group(1)的结果
            bm = re.match(r'^([^-]+-[^-]+-[^-]+)', bp).group(1)
            bs = generate_random_string()
            print('自动生成的序列号是:%s'%bs)
            check = input("即将刷写的内容如下:\n制造商信息(BM、SM）:%s\n产品信息(BP、SP）: "
                          "%s\n产品版本（BV、SV）: "
                          "%s\n产品序列号(BS、SS）: "
                          "%s\n请核对!("
                          "y/n)"
                          % (bm, bp, bv, bs))

print("接下来将开始BIOS刷入,请等待...")

# AMIDEWINX64在部分主板有BUG，只能依次刷写，所以这样写

cmd1 = "AMIDEWINx64.EXE /BM %s" % bm
cmd2 = "AMIDEWINx64.EXE /BP %s" % bp
cmd3 = "AMIDEWINx64.EXE /BV %s" % bv
cmd4 = "AMIDEWINx64.EXE /BS %s" % bs
cmd5 = "AMIDEWINx64.EXE /SM %s" % bm
cmd6 = "AMIDEWINx64.EXE /SP %s" % bp
cmd7 = "AMIDEWINx64.EXE /SV %s" % bv
cmd8 = "AMIDEWINx64.EXE /SS %s" % bs

sys(cmd1)
sys(cmd2)
sys(cmd3)
sys(cmd4)
sys(cmd5)
sys(cmd6)
sys(cmd7)
sys(cmd8)

print("BIOS刷入完毕,请检查是否刷入正确:")
sys("AMIDEWINx64.EXE /BM\n")
sys("AMIDEWINx64.EXE /BP\n")
sys("AMIDEWINx64.EXE /BV\n")
sys("AMIDEWINx64.EXE /BS\n")
sys("AMIDEWINx64.EXE /SM\n")
sys("AMIDEWINx64.EXE /SP\n")
sys("AMIDEWINx64.EXE /SV\n")
sys("AMIDEWINx64.EXE /SS\n")
print("按ESC退出程序.")
sys('pause>nul')