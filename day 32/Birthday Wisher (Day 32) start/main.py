#SMTP - Simple Mail Transfer Protocol
import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 6:
    with open("D:\\100P\\day 32\\Birthday Wisher (Day 32) start\\quotes.txt", "r") as data:
        quotes = data.read().splitlines()
        random_quote = choice(quotes)

    my_email = "mname5121@gmail.com" # part before @ is identity of my email and the part after @ is identity of the email provider
    password = "zhckvkgkaycgcgbf"


    # for gmail - smtp.gmail.com
    # for hotmail - smtp.live.com
    # for yahoo - smtp.mail.yahoo.com

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # TLS - Transport Layer Security - Way of securing our connection to our email server if this functionality is enable the contents were encrypted to the intruder
        connection.starttls() 
        connection.login(user=my_email, password=password) 
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="mname5121@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
            )







# date_of_birth = dt.datetime(year=2003, month=1,day=14,hour=4)
# print(date_of_birth)

# year = now.year
# month = now.day
# print(month)