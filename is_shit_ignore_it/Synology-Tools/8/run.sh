#!/bin/sh

./qh_iops_dir.py >> fio.log && ./qh_smb_1m_directory.py >> fio.log && ./qh_smb_1m_file.py >> fio.log && ./qh_smb_64k_directory.py >> fio.log && ./qh_smb_64k_file.py >> fio.log

echo "\033[36;1miops路径模式测试完毕,请删除分区后进行设备模式测试,准备好后手动运行./qh_iops_dev.py"
