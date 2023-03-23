import os, keyboard, time


def menu():
    print(
        """
    功能菜单：
    1.  FIO性能测试
    2.  硬盘压测
    3.  网络测试

    请按对应序号进行选择：
    """
    )

    while True:
        ch = input()
        match ch:
            case "1":
                fio()
                break
            case "2":
                print("进入硬盘压测菜单！")
                break
            case "3":
                print("进入网络测试")
                break
            case _:
                print("你要不看看你选的啥？\n重新选择：")


def fio():
    ch_nas = input(
        """
    欢迎使用FIO性能测试！
    请选择测试的NAS型号：
    1.  YGENAS-V-H8
    2.  YGENAS-R-H12
    3.  YGENAS-R-H16
    4.  YGENAS-R-H24
    5.  YGENAS-R-H36
    """
    )
    match ch_nas:
        case "1":
            print("8盘位")
        case "2":
            print("12盘位")
        case "3":
            print("16盘位")
        case "4":
            print("24盘位")
        case "5":
            print("36盘位")
        case _:
            print("输入错误，程序终止！")


if __name__ == "__main__":
    os.system(
        "echo \033[31;1mIf Chinese cannot be displayed normally, please use "
        "the client that supports Chinese display to connect remotely and run the tool again! &&sleep 2s"
    )
    os.system(
        """
    echo \033[32;1m欢迎使用YGENAS-autoTestTool！\n
    本工具集成了多项功能，自行选择即可！\n
    \033[31;1m测试工作开始前，请务必确保你已完全了解测试工作内容，各测试项区别，测试注意事项！\n
    \033[31;1m确认开始按Enter，退出按Esc！
    """
    )

    while True:
        if keyboard.is_pressed("enter"):
            os.system("echo \033[32;1m已收到确认指令，程序开始执行：")
            for i in range(3, 0, -1):
                print("%ss" % i)
                time.sleep(1)
        elif keyboard.is_pressed("esc"):
            exit()
        break

    menu()
