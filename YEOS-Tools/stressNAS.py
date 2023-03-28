#!/usr/bin/python3

import subprocess, re


def randrw():
    # 初始化用于存储运行结果的列表
    bw = [0, 0, 0, 0, 0, 0]
    iops = [0, 0, 0, 0, 0, 0]
    # fio重复运行4次
    print("随机读写进行中...")
    cmd = [
        "fio",
        "-name=YEOS",
        "-size=32G",
        f"-runtime={stress_time}",
        "-bs=4k",
        "-direct=1",
        "-rw=randrw",
        "-ioengine=libaio",
        f"-numjobs={stress_disk}",
        "-group_reporting",
        "-iodepth=64",
        f"-filename={stress_dir}",
        "-rwmixwrite=30",
    ]

    # 将fio运行结果标准输出到管道
    fio1 = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)

    fio2 = subprocess.Popen(
        ["grep", "samples"], stdin=fio1.stdout, stdout=subprocess.PIPE, shell=False
    )

    # 使用communicate获取子进程的标准输出并格式化为utf-8编码
    fio = fio2.communicate()[0].decode("utf-8")

    # 初始化列表
    bw_num = []
    iops_num = []
    # 匹配数字和小数点，并将其元素更新
    for line in fio.split("\n"):
        if "bw" in line:
            bw_num.extend(re.findall(r"\d+\.\d+|\d+", line))
        elif "iops" in line:
            iops_num.extend(re.findall(r"\d+\.\d+|\d+", line))

    # 将str类型转换为float后再转换为int
    bw_num = [int(float(e)) for e in bw_num]
    iops_num = [int(float(e)) for e in iops_num]

    print(
        f"随机读写均值如下:\n"
        f"读:\n带宽最小值:{bw_num[0]},最大值{bw_num[1]},均值{bw_num[3]}\nIOPS最小值:{iops_num[5]},"
        f"最大值{iops_num[6]},均值{iops_num[7]}"
        "\n"
        f"写:\n带宽最小值:{bw_num[6]},最大值{bw_num[7]},均值{bw_num[9]}\nIOPS最小值"
        f":{iops_num[0]},"
        f"最大值{iops_num[1]},均值{iops_num[2]}"
    )


if __name__ == "__main__":
    print(
        """
        欢迎使用YEOS硬盘压测工具！
        使用本工具前，需要设置压测路径、硬盘数量、时间
    """
    )
    stress_dir = input("请输入压测路径:")
    stress_time = input("请输入压测时间[秒:s 分:m 时:h]:")
    stress_disk = input("请输入硬盘数量:")
    print("开始压测！\n务必等待压测结束并输出运行结果！\n不可中途停止！\n压测结束后需要删除压测所用池！")
    randrw()
