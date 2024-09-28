import smtplib
from datetime import datetime
import pandas as pd
import random

MY_EMAIL = "qsimran08@gmail.com"
MY_PASSWORD = "canl vrky hsql uzjq"

now = datetime.now()
today = (now.month, now.day)
# print(now)
data = pd.read_csv('birthdays.csv')

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# read note on iterrows()

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]  # will access data row
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as letter_file:
        old_content = letter_file.read()
        content = old_content.replace("[NAME]" , birthday_person["name"]) #store replace() in a var or else it won't replace any string

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject: Happy Birthday \n\n{content}")