#!/usr/bin/env python3

import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#  for gmail --> smpt.gmail.com  PORT 587
# One needs an internet connection else an socket Errno:11044 will be raised

smtpObj.ehlo()

# Starting the TLS Encryption
# This will ensure your SMTP connection is in TLS mode.
smtpObj.starttls()

MY_MAIL_ADDRESS = input("Enter your valid Gmail address")
PASSWORD = input("Enter your above email password")
RECIEVER_EMAIL_ID = input("Enter the reciever Email Address")
# Loging in 

smtpObj.login(MY_MAIL_ADDRESS, PASSWORD)

Message = input("Enter the message you want to send")
for i in range(0,10):
    smtpObj.sendmail(MY_MAIL_ADDRESS, RECIEVER_EMAIL_ID, f'Subject:\n{Message}')

smtpObj.quit()




