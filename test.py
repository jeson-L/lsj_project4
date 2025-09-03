import shutil
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    # 打包
    shutil.make_archive("./report/html_report", 'zip', './report/html_report')
    config = {
        "smtp_server": "smtp.qq.com",
        "smtp_port": 465,
        "render_email": '841379286@qq.com',
        "password": 'djnkfvwgiqyrbchj',
        "receiver_email": '841379286@qq.com'
    }
    msg = MIMEMultipart()
    msg['From'] = config['render_email']
    msg['To'] = config['receiver_email']

    with open(r'./report/html_report.zip', 'rb') as f:  # ← 这里指定文件路径
        file_data = f.read()
    attachment = MIMEApplication(file_data)
    attachment.add_header('Content-Disposition', 'attachment', filename='html_report.zip')
    msg.attach(attachment)

    server = smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'])
    server.login(config['render_email'], config['password'])
    server.send_message(msg)


if __name__ == '__main__':
    send_email()
