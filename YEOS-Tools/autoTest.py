import subprocess, re


# TODO 将下列代码包装为传参函数
def fio_cmd(size, bs, rw, numjobs, filename_or_directory, myDir):
    # 初始化用于存储运行结果的列表
    bw = [0, 0, 0]
    iops = [0, 0, 0]

    # fio重复运行4次
    for i in range(4):
        # TODO 调试完毕后将runtime改回60s
        cmd = [
            "fio",
            "-name=YEOS",
            f"-size={size}G",
            "-runtime=5s",
            f"-bs={bs}",
            "-direct=1",
            f"-rw={rw}",
            "-ioengine=libaio",
            f"-numjobs={numjobs}",
            "-group_reporting",
            "-iodepth=64",
            f"-{filename_or_directory}={myDir}/{i}",
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
        if i == 0:
            continue
        else:
            # 将每次运行结果保存到列表
            bw[0] += bw_num[0]
            bw[1] += bw_num[1]
            bw[2] += bw_num[3]
            iops[0] += iops_num[0]
            iops[1] += iops_num[1]
            iops[2] += iops_num[2]
        print(
            f"第{i + 1}次运行结果如下:\n带宽最小值:{bw_num[0]},最大值{bw_num[1]},"
            f"均值{bw_num[3]}\niops最小值:{iops_num[0]},最大值{iops_num[1]},"
            f"均值{iops_num[2]}"
        )

    bwMin = int(bw[0] / 3)
    bwMax = int(bw[1] / 3)
    bwAvg = int(bw[2] / 3)
    iopsMin = int(iops[0] / 3)
    iopsMax = int(iops[1] / 3)
    iopsAvg = int(iops[2] / 3)

    print(
        f"均值如下:\n带宽最小值:{bwMin},最大值{bwMax},均值{bwAvg}\nIOPS最小值:{iopsMin},"
        f"最大值{iopsMax},均值{iopsAvg}"
    )


def fio_choose():
    test_type = input("测试类型:\n1.IOPS\n2.带宽\n3.全部")
    sync_mode = input("同步模式:\n1.standard\n2.disable")
    if test_type == "1":
        block_size = input("逻辑块大小:\n1.512B\n2.4K")
    elif test_type == "2":
        record_size = input("记录大小:\n1.128K\n2.1M")
    elif test_type == "3":
        block_size = input("逻辑块大小:\n1.512B\n2.4K")
        record_size = input("记录大小:\n1.128K\n2.1M")


if __name__ == "__main__":
    fio_cmd("100G", "4k", "randwrite", 12, "filename", "/data")


# TODO 将最终结果直接输出到Excel表格
