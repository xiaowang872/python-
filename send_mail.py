"""
This module contains functions related to historical QQ numbers.

Author: wangguixiang
Email: 2826551098@qq.com
Date: 2024-10-22
"""


import smtplib
from email.message import EmailMessage

textfile = 'email.html'

# 打开文本文件并读取内容
with open(textfile, 'r', encoding='utf-8') as fp:  # 确保指定正确的编码，如 utf-8
    content = fp.read()

# 创建邮件消息
msg = EmailMessage()
msg.set_content(content)
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = '***********@qq.com'
msg['To'] = '222222@qq.com'
#
# 连接到 QQ 邮箱的 SMTP 服务器，使用 SSL
try:
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:  # 使用 SMTP_SSL 类并指定端口 465
        # 登录到 SMTP 服务器，使用您的邮箱地址和授权码（不是密码）
        server.login('********@qq.com', '**********')  # 替换 '**********' 为您的授权码
        # 发送邮件
        server.send_message(msg)
        print("邮件发送成功！")
except Exception as e:
    print(f"发送邮件时执行状态: {e}")