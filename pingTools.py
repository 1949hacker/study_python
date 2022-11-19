from ping3 import ping

# 功能列表
iCanDo = {1: "网络连通性", 2: "网络稳定性", "结束":"请输入quit"}

print("欢迎使用网络ping检测工具                 \n                                  ——Vladimir.1949HACKER\n\n\n本工具可以检测的有：")
for a, b in iCanDo.items():
    print(a, b)

while 1 == 1:
    print("请选择您要使用的功能，输入数字即可：")
    choice = input()
    match choice:
        case "1":
            ip = input("请输入您要检测的IP或域名：")
            if ping(ip) is False:
                print("\n\n目标地址无法访问！\n检测完毕！返回选择菜单")
            else:
                print("\n\n目标地址通信成功！\n检测完毕！返回选择菜单")

        case "2":
            ip = input("请输入您要检测的IP或域名：")
            times = int(input("探测多少次："))
            pingIp = 0
            delays = 0
            max = 0
            min = 99999
            for i in range(1, times+1):
                if pingIp > max:
                    max = pingIp
                elif pingIp < min:
                    min = pingIp
                else:
                    max = max
                    min = min
                pingIp = ping(ip, unit="ms")
                delays = pingIp + delays
                print("第%s次探测延迟：%.2f毫秒" % (i, pingIp))
            delay = delays/times
            print("\n\n共检测%s次，检测结果如下：\n平均延迟是：%.2f毫秒\n最大延迟是：%.2f毫秒\n最小延迟是：%.2f毫秒\n检测完毕！返回选择菜单" % (times, delay, max, min))

        case "quit":
            break

        case other:
            print("您的输入有误！")
