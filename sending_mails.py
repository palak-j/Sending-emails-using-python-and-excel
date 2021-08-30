import pandas as pd

import smtplib


file = pd.read_csv("E:\mails.csv")

receivers = list(file['mail_id'])


gmail_user = 'jainpalak741@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to = receivers
subject = 'Sending mail using excel and python'
body = 'This is a test e-mail.'

email = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email)
    smtp_server.close()
    print ("Email successfully sent!!")
except Exception as ex:
    print ("Something went wrong!!",ex)



