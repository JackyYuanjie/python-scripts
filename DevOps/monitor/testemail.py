# -*- coding:utf-8 -*-

# 安装: pip install yagmail
import yagmail

try:
    # 使用yagmail的类创建对象(发件人,发件人授权码，发件的服务器)
    # 发件人授权码: password="JackyLi666"
    yagobj = yagmail.SMTP(user="13641323756@163.com",password="JackyLi666",host="smtp.163.com")
    # 使用yagobj对象发送邮件(指定收件人，邮件主题--发送内容)
    content = "测试发送邮件是否正常."
    yagobj.send("devops_yj@163.com","测试邮件",content)
except BaseException as e:
    print(e)


