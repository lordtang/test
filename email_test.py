# coding=utf-8
import smtplib
from email.mime.text import MIMEText

def send_test_html(msg):
    '''
    参数：需要发送的消息/html文件
    返回值：无
    功能：向指定邮箱发送一篇纯文本或者二进制html文件的邮件
    相关配置：请在config中修改相关配置参数
    注意：使用前请修改该函数的config参数，包括发送方，接收方，发送数据类型等参数
    '''


    config = {
        "sender":'2398504790@qq.com',
        "password":'mcujhkirmijoebif',
        'receiver':'cdutangliang@sina.com',
        'smtp_server':'smtp.qq.com',
        'subject':'from test department',
        'port':465,
        'type':'html'
    }

    sender = config['sender']
    password = config['password']
    receiver = config['receiver']
    smtp_server =config['smtp_server']
    subject = config['subject']
    port = config['port']
    type_of_msg=config['type']

    msg = MIMEText(msg,type_of_msg,'utf-8')
    #发送邮箱地址
    msg['From'] = sender
    #收件箱地址
    msg['To'] = receiver
    #主题
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP_SSL(smtp_server,port)
    except Exception as e:
        print("创建服务出错",e)
        return

    try:
        server.login(sender,password)
        server.sendmail(sender,receiver,msg.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败",e)
    finally:
        server.quit()

if __name__ == "__main__":
    with open('./python_html.html','rb') as f:
        html = f.read()
        send_test_html(html)
