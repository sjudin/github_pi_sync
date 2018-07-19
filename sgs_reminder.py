#!/usr/bin/python3
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sys.argv[1], sys.argv[2])

msg = MIMEMultipart()
msg['From'] = sys.argv[1]
msg['To'] = sys.argv[1]
msg['Subject'] = "Log into SGS to renew membership"


body = "Log into SGS so you dont lose your days! link: https://www.sgsstudentbostader.se/?sc_lang=sv-SE"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
server.sendmail(sys.argv[1], sys.argv[1], text)
server.quit()
