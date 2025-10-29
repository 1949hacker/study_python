import subprocess
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def get_hostname():
    # 获取当前主机名
    hostname = socket.gethostname()
    return hostname

def run_chkrootkit():
    # 运行chkrootkit命令并获取输出
    result = subprocess.run(['chkrootkit'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output = result.stdout + result.stderr
    # 将输出结果保存到文件
    with open('/var/log/chkrootkit.log', 'w') as f:
        f.write(output)
    return '/var/log/chkrootkit.log'

def send_email(attachment_path, recipient_email, hostname):
    # 电子邮件设置
    sender_email = "0@hackerbs.com"
    sender_password = "null"
    subject = hostname + "\'s chkrootkit log"
    body = "Please find the attached chkrootkit output."

    # 创建电子邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 添加附件
    with open(attachment_path, 'rb') as f:
        part = MIMEApplication(f.read(), Name='chkrootkit_output.txt')
        part['Content-Disposition'] = 'attachment; filename="chkrootkit_output.txt"'
        msg.attach(part)

    # 发送邮件
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls
