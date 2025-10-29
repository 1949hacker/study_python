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
        cpu_usage = psutil.cpu_percent(interval=1)  # 获取 CPU 使用率
        print(f"CPU freq: {cpu_freq.current} MHz, CPU usage: {cpu_usage}%")
        time.sleep(1)


def display_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)  # 获取 CPU 使用率
        print(f"CPU usage: {cpu_usage}%")
        time.sleep(1)


def main():
    print("1. Display CPU Frequency")
    print("2. Stress CPU and display freq")
    print("3. Display CPU Usage")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_cpu_frequency()
    elif choice == 2:
        cpu_stress_test()
    elif choice == 3:
        display_cpu_usage()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
