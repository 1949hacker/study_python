import os
import queue
import random
import socket
import struct
import threading
import time


def checksum(msg):
    """TCP 以及 IP校验和"""
    s = 0
    # 每次取2个字节
    for i in range(0, len(msg), 2):
        w = (msg[i] << 8) + (msg[i + 1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s


class SynScan:
    def __init__(self, ip_list, port_list, rate=2000, timeout=5):
        self.ips = ip_list
        self.ports = port_list
        self.timeout = timeout
        self.socket = self._socket()
        self.rate = rate
        self.src_ip = None
        self.finished = False

        if not self.get_local_ip():
            print("请检查网络......")
            os._exit(1)
        self.seq = random.randint(1000000000, 2000000000)

        # 获取本地IP
    def get_local_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("8.8.8.8", 0))
            self.src_ip = s.getsockname()[0]
            return True
        except:
            pass
        return False

        # 创建IP包
    def ip_headers(self, src_ip, dst_ip):
        hl_version = (4 << 4) + 5
        diff = 0
        total_len = 40
        ident = random.randint(18000, 65535)
        flags = 0
        offset = 0
        ttl = 255
        protocol = 6
        check = 0
        src_addr = socket.inet_aton(src_ip)
        dst_addr = socket.inet_aton(dst_ip)
        buffer = struct.pack('!BBHHBBBBH4s4s', hl_version, diff, total_len,
                             ident, flags, offset, ttl, protocol, check, src_addr, dst_addr)
        checkSum = checksum(buffer)
        _header = struct.pack('!BBHHBBBBH4s4s', hl_version, diff, total_len,
                              ident, flags, offset, ttl, protocol, checkSum, src_addr, dst_addr)
        return _header

        # 创建TCP包
    def tcp_headers(self,  src_ip, dst_ip, src_port, dst_port):
        seq = self.seq
        ack_seq = 0
        doff = 5
        check = 0
        offset_res = (doff << 4) + 0
        fin, syn, rst, psh, ack, urg = (0, 1, 0, 0, 0, 0)
        tcp_flags = fin + (syn << 1) + (rst << 2) + \
            (psh << 3) + (ack << 4) + (urg << 5)
        window = 1024
        urg_ptr = 0
        tcp_header = struct.pack('!HHLLBBHHH', src_port, dst_port, seq,
                                 ack_seq, offset_res, tcp_flags, window,  check, urg_ptr)
        # 伪头部选项 源IP地址(4字节)、目的IP地址(4字节)、协议(2字节)、TCP/UDP包长(2字节)
        source_address = socket.inet_aton(src_ip)
        dest_address = socket.inet_aton(dst_ip)
        protocol = 6
        tcp_length = len(tcp_header)
        psh = struct.pack('!4s4sHH', source_address,
                          dest_address, protocol, tcp_length)
        psh = psh + tcp_header
        tcp_checksum = checksum(psh)
        tcp_header = struct.pack('!HHLLBBHHH', src_port, dst_port, seq,
                                 ack_seq, offset_res, tcp_flags, window, tcp_checksum, urg_ptr)
        return tcp_header

    def _socket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                              socket.IPPROTO_TCP)  # raw socket 创建
            s.setsockopt(socket.IPPROTO_IP,
                         socket.IP_HDRINCL, 1)  # 可自定义 IP头部信息
            s.settimeout(self.timeout)

            return s
        except:
            # print(e)
            return self._socket()

    def recv_packet(self, src_port):
        while 1:
            try:
                recv_packet, addr = self.socket.recvfrom(1024)
                _ip = addr[0]  # ip 信息
                ack_seq = struct.unpack("!L", recv_packet[28:32])[0]  # 回答的seq
                s_port = struct.unpack("!H", recv_packet[20:22])[0]  # 包内源端口
                d_port = struct.unpack("!H", recv_packet[22:24])[0]  # 包内目的端口
                if src_port == d_port and ack_seq == self.seq + 1:
                    if recv_packet[33] == 18:  # 18 代表回包 syn 和 ack 确认包， 端口开放
                        #print(f"地址:{_ip}  开放端口:{s_port}")
                        print(f"{_ip}")
            except:
                pass
            if self.finished:
                break

    def start(self):
        src_port = random.randint(30000, 60000)  # 随机一个源端口
        t = threading.Thread(target=self.recv_packet, args=(src_port, ))
        t.start()
        time_sleep = 1 / self.rate
        failed_packet = queue.Queue()
        for ip in self.ips:
            for port in self.ports:
                packet = self.ip_headers(
                    self.src_ip, ip) + self.tcp_headers(self.src_ip, ip, src_port, port)
                try:
                    self.socket.sendto(packet, (ip, 0))  # 因为某些操作系统协议栈问题，可能会失败
                except Exception as e:
                    failed_packet.put((ip, packet))
                time.sleep(time_sleep)

        while not failed_packet.empty():  # 重新发送失败的队列数据
            ip, packet = failed_packet.get()
            try:
                self.socket.sendto(packet, (ip, 0))
            except:
                failed_packet.put((ip, packet))
            time.sleep(time_sleep)

        time.sleep(self.timeout+1)
        self.finished = True
        self.socket.close()


if __name__ == '__main__':

    ip_list = ['8.128.'+str(c)+'.'+str(d)
               for c in range(0, 255)for d in range(1, 255)]
    port_list = [22]
    synScan = SynScan(ip_list, port_list)
    synScan.start()
