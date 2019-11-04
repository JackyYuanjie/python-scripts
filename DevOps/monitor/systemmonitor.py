# -*- coding:utf-8 -*-
import psutil
import datetime
import yagmail



# 定时监控
def WindowMonitor(time):
    """定义函数,获取windows系统的硬件信息"""
    # cpu使用率
    cpuuse = psutil.cpu_percent(interval=time)

    # 内存信息
    memoryinfo = psutil.virtual_memory()

    # 磁盘信息
    diskinfo = psutil.disk_usage("/")

    # 网络信息
    networkinfo = psutil.net_io_counters()

    # 获取系统当前时间
    nowtime = datetime.datetime.now().strftime("%F %T")

    # 拼接字符串显示
    log_str =  "|--------------------|-----------|--------------|--------------|-----------------------|\n"
    log_str += "|     监控时间       | cpu使用率 |  内存使用率  |  磁盘使用率  |       网络使用率      |\n" 
    log_str += "|                    |(共%d核cpu) | (总计%dG内存)|(总计%dG硬盘)|                       |\n"% (psutil.cpu_count(logical=False),\
        float(memoryinfo.total/1024/1024/1024),diskinfo.total/1024/1024/1024)
    log_str += "|--------------------|-----------|--------------|--------------|-----------------------|\n"
    log_str += "| %s|   %s%%   |     %s%%    |   %s%%      | 收:%s/发:%s|\n" %(nowtime,cpuuse,memoryinfo.percent,diskinfo.percent,networkinfo.bytes_recv,networkinfo.bytes_sent)
    log_str += "|--------------------|-----------|--------------|--------------|-----------------------|\n"
    # print(log_str)

    # 保存到文件中
    txtsave = "F:\\PythonProject\\python-scripts\\DevOps\\monitor\\systemmonitor.txt"
    with open(txtsave,"a",encoding="utf-8") as f:
        f.write(log_str + "\n\n")

    if cpuuse > 80 or memoryinfo.percent > 85:
    # 发送邮件
        yagobj = yagmail.SMTP(user="13641323756@163.com",password="JackyLi666",host="smtp.163.com")
        yagobj.send("devops_yj@163.com","windows系统监控信息",log_str)

def main():
    # while True:
        # WindowMonitor(10)
    WindowMonitor(10)

print(__name__)
if __name__=="__main__":
    main()
