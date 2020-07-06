import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#  for gmail --> smpt.gmail.com  PORT 587

# One needs an internet connection else an socket Errno:11044 will be raised

smtpObj.ehlo()

# Starting the TLS Encryption

smtpObj.starttls()
# This will ensure your SMTP connection is in TLS mode.

MY_MAIL_ADDRESS = input("Enter your valid Gmail address")
PASSWORD = input("Enter your mail password")
# Loging in 

smtpObj.login(MY_MAIL_ADDRESS, PASSWORD)


