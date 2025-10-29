#!/usr/bin/python3

import subprocess, re


def randrw():
    # 初始化用于存储运行结果的列表
    bw = [0, 0, 0, 0, 0, 0]
    iops = [0, 0, 0, 0, 0, 0]
    # fio重复运行4次
    print("randrw is running...")
    cmd = [
        "fio",
        "-name=YEOS",
        "-size=32G",
        f"-runtime={stress_time}",
        "-time_base",
        "-bs=4k",
        "-direct=1",
        "-rw=randrw",
        "-ioengine=libaio",
        f"-numjobs={stress_disk}",
        "-group_reporting",
        "-iodepth=64",
        f"-filename={stress_dir}/test",
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
        f"randrw results:\n"
        f"read:\nbw min:{bw_num[0]},max{bw_num[1]},av"
        f"g{bw_num[3]}\nIOPS min"
        f":{iops_num[5]},"
        f"max{iops_num[6]},avg{iops_num[7]}"
        "\n"
        f"write:\nbw min:{bw_num[6]},max{bw_num[7]},avg{bw_num[9]}\nIOPS min"
        f":{iops_num[0]},"
        f"max{iops_num[1]},avg{iops_num[2]}"
    )


if __name__ == "__main__":
    print(
        """
        welcome to use YEOS disk stress tool!
        Before use,You need set stress dir,disk and runtime
    """
    )
    stress_dir = input(
        "Please input stress dir[must enter an absolute path,is like this: "
        "/mnt/test/]:"
    )
    stress_time = input(
        "Please input stress tool runtime[seconds:s minutes:m hours:h],"
        "is like this: 24h,Indicates run 24 hours:"
    )
    stress_disk = input("Please input stress disk[just input number,is like this:8]:")
    print(
        f"Stress is started...\nYou must wait for the program to finish "
        "running!\nIf you stop halfway, you need to manually delete the test "
        f"file under {stress_dir}."
    )
    randrw()
    rm_stressFile = subprocess.Popen(
        ["rm", "-rf", f"{stress_dir}/*"], stdout=subprocess.PIPE, shell=False
    )
    rm_stressFile.wait()
    print(
        f"The test file has been deleted, but please check again to see if "
        f"there are still any residues in the {stress_dir} directory."
    )
