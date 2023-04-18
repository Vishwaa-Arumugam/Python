import pandas
import datetime as dt
from random import choice
import smtplib

data = pandas.read_csv("D:\\100P\\day 32\\birthdays.csv")
date_data = data["day"].to_list()
month_data = data["month"].to_list()
year_data = data["year"].to_list()
name_data = data["name"].to_list()
email_data = data["email"].to_list()

day_1 = date_data[0]
month_1 = month_data[0]
year_1 = year_data[0]
name = name_data[0]
email = email_data[0]

month = int("{:.0f}".format(month_1))
day = int("{:.0f}".format(day_1))
year = "{:.0f}".format(year_1)

now = dt.datetime.now()
today_year = now.year
today_month = now.month
today_day = now.date().day

if today_day == day and today_month == month:
    letter = ["D:\\100P\\day 32\\letter_templates\\letter_1.txt", "D:\\100P\\day 32\\letter_templates\\letter_2.txt",
              "D:\\100P\\day 32\\letter_templates\\letter_3.txt"]
    letter_choice = choice(letter)

    with open(letter_choice, "r") as bday_card:
        data = bday_card.read()
        data = data.replace('[NAME]', name)

    my_email = "mname5121@gmail.com"
    password = "zhckvkgkaycgcgbf"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{data}"
        )
