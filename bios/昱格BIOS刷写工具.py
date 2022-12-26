from os import system as sys

sys("@echo off")
sys("color 0a")
sys("title 昱格BIOS刷写工具")

print("欢迎使用昱格BIOS刷写工具\n在开始之前,需要设定几个参数的值.\nBP 产品的名称,命名规则为YGENAS-桌面式V/机架式R-盘位数量（Hx）-型号（ A-Z）\nBV 产品的版本,如V1.0\nBS 产品的序列号,使用SNCreator生成.")
bm = "YGENAS"

check = 'n'
while check == 'n':
    match check:
        case 'y':
            break
        case 'n':
            bp = input("请输入BP参数的值:")
            bv = input("请输入BV参数的值:")
            bs = input("请输入BS参数的值:")
            check = input("您输入的值分别是:\nBP: %s\nBV: %s\nBS: %s\n请核对!(y/n)" % (bp,bv,bs))

print("接下来将开始BIOS刷入,请等待...")

command = 'AMIDEWINx64.EXE /BM "%s" /BP "%s" /BV "%s" /BS "%s"' % (bm,bp,bv,bs)
print(command)
sys(command)

print("BIOS刷入完毕,请检查是否刷入正确:")
sys('AMIDEWINx64.EXE /BM /BP /BV /BS')
print("按ESC退出程序.")
sys('pause>nul')