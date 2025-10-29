from os import system as sys
import uuid
import platform
import distro


def convert_uuid():
    uuid_obj = uuid.uuid4()
    print("UUID:", uuid_obj)
    bytes_array = uuid_obj.bytes
    result = []
    for byte in bytes_array:
        result.append(hex(byte))
    return " ".join(result)


def flush_UUID():
    sys("linux/amiTool/afuForLinux_x64 bios /P /B /N /R /X")
    sys("ipmitool raw 0x6 0x52 0x0b 0xae 0x0 0x0f 0x00" + convert_uuid())


def init_deb():
    sys("dpkg -i linux/deb/*.deb")
    sys("modprobe ipmi_devintf")
    sys("modprobe ipmi_watchdog")
    sys("modprobe ipmi_poweroff")
    sys("modprobe ipmi_msghandler")


def detect_os():
    os_type = platform.system()
    if os_type == 'Windows':
        return "本工具仅支持Debian bookworm系统"
    elif os_type == 'Linux':
        distro_info = distro.id()
        if distro_info in ['debian', 'ubuntu']:
            return "pass"
        else:
            return "本工具仅支持Debian bookworm系统"
    else:
        return "本工具仅支持Debian bookworm系统"


print("欢迎使用昱格BIOS System UUID刷写工具\n本工具会自动先刷写BIOS，然后调用ipmitool刷写UUID，刷写完成重启后dmidecode -s "
      "system-uuid的值便会变化。\n刷写之前，需要将BIOS固件重命名为bios，放到和本工具相同的目录下才可自动识别。")
print("系统检测：", detect_os())
print("转换后UUID：", convert_uuid())
init_deb()
flush_UUID()
print("BIOS和UUID刷写完毕，系统即将重启")
sys("sleep 2s")
sys("reboot")