# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

"""
# sendmail访问方法:

sender = "13641323756@163.com"  # 发送邮件的账号
# 接收邮件的邮箱账号.
receivers = ["devops_yj@163.com","1976475582@qq.com"]  

# 第一个参数: 设置文本内容,第二个参数:plain设置文本格式
message = MIMEText('smtp代码测试',"plain","utf-8")
message['From'] = Header("py代码","utf-8")
message['To'] = Header("测试","utf-8")

subject = "smtp代码测试"
message['Subject'] = Header(subject,"utf-8")

try:
    # 实例化SMTP对象smtpobj连接SMTP访问.
    smtpobj = smtplib.SMTP("smtp.163.com")
    # 使用sendmail来发送信息.
    smtpobj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功.")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

"""

# 使用其他服务商的SMTP访问
mail_host = "smtp.163.com"  # 设置163的服务器
mail_user = "devops_yj@163.com"
mail_pass = "devops"

# 发送邮件的邮箱地址
sender = "devops_yj@163.com"
# 接收邮件的邮箱地址
receivers = ['13641323756@163.com']

message = MIMEText('Python邮件测试...','plain','utf-8')
message['From'] = Header("测试smtp代码","utf-8")
message['To'] = Header("sendmails脚本代码","utf-8")

subject = "邮件代码测试"
message['Subject'] = Header(subject,"utf-8")

try:
    smtpobj = smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功.")
except smtplib.SMTPException as e:
    print(e)