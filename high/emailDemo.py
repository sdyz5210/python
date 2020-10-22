#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "xxxx@163.com"  # 用户名
mail_pass = "xxxx"  # 口令

sender = 'xxxx@163.com'
receivers = ['xxxxxxxxx@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')   # 发送者
message['To'] = Header("测试", 'utf-8')        # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP(mail_host)
    smtpObj.login(mail_user, mail_pass) 
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
