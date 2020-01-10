# -*- coding:utf-8 -*-

# 安装: pip install yagmail
import yagmail

try:
    # 使用yagmail的类创建对象(发件人,发件人授权码，发件的服务器)
    # 发件人授权码: password="xxx"
    yagobj = yagmail.SMTP(user="xxxxxx@163.com",password="xxx",host="smtp.163.com")
    # 使用yagobj对象发送邮件(指定收件人，邮件主题--发送内容)
    content = "测试发送邮件是否正常."
    yagobj.send("xxxxxx@163.com","测试邮件",content)
except BaseException as e:
    print(e)


