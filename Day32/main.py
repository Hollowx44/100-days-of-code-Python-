import pandas
import random
import smtplib
import datetime as dt

def send(letter,email):
    my_email="test_email_here@gmail.com"
    password="app_password_here"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"subject:Happy Birthday {i["name"]}\n\n{letter}")
        print("Done")

now=dt.datetime.now()
day=now.day
month=now.month
bdays=pandas.read_csv("birthdays.csv")
bdays_list=bdays.to_dict(orient="records")
for i in bdays_list:
    if day == i["day"] and month == i["month"]:
        email=i["email"]
        choosing_letter=random.randint(1,3)
        with open(f"letter_templates/letter_{choosing_letter}.txt") as choosen_letter:
            final_letter=choosen_letter.read()
            final_letter=final_letter.replace("[NAME]",i["name"])
            send(final_letter,email)