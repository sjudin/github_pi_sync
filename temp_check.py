#!/usr/bin/python3
import smtplib
import os
import time
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

time.sleep(15)

test = True

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sys.argv[1], sys.argv[2])

msg = MIMEMultipart()
msg['From'] = sys.argv[1]
msg['To'] = sys.argv[1]
msg['Subject'] = "Raspberry overheated"


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return int(temp.replace("temp=", "").replace("'C", "''").split('.')[0])


while True:
    if measure_temp() > 83:
        body = str("Raspberry at home has overheated at " + str(datetime.now()) + ', script has shut down, remember to start it up again')
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(sys.argv[1], sys.argv[1], text)
        break

    time.sleep(3)

server.quit()
