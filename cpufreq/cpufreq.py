import psutil
import time
import multiprocessing


def display_cpu_frequency():
    while True:
        cpu_freq = psutil.cpu_freq()
        print(f"CPU freq: {cpu_freq.current} MHz")
        time.sleep(1)


def cpu_stress():
    while True:
        # 进行一些复杂的计算以增加 CPU 负载
        x = 0
        for i in range(10 ** 8):
            x += i


def cpu_stress_test():
    print("start CPU stress...")
    processes = []
    for _ in range(multiprocessing.cpu_count()):  # 创建与 CPU 核心数相同的进程
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    while True:
        cpu_freq = psutil.cpu_freq()
        print(f"CPU freq: {cpu_freq.current} MHz")
        time.sleep(1)

        choice = input("wanna stop？(y/n)")
        if choice.lower() == 'y':
            for p in processes:
                p.terminate()  # 结束压测进程
            break


def main():
    print("1. CPU freq")
    print("2. Stress CPU")
    choice = int(input("choice: "))

    if choice == 1:
        display_cpu_frequency()
    elif choice == 2:
        cpu_stress_test()
    else:
        print("WTF?")


main()
