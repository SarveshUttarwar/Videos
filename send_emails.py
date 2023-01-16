import smtplib, ssl
host = "smtp.gmail.com"
port = 465

username = "sarveshuttarwar3@gmail.com"
password = "csqywoajwifreiow"

receiver = "sarveshuttarwar3@gmail.com"
context_fun = ssl.create_default_context()

message =""""
Hi! 
HOW ARE YOU?
BYE
"""
with smtplib.SMTP_SSL(host,port,context = context_fun) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)