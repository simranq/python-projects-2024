# CHALLENGE 1: MONDAY MOTIVATIONAL QUOTE GENERATOR

import datetime as dt
from random import choice
import smtplib

MY_EMAIL = "qsimran08@gmail.com"
MY_PASSWORD = "canl vrky hsql uzjq"
RECEIVERS_EMAIL = "seojaerinn14@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVERS_EMAIL,
            msg = f"Subject:Monday Motivation\n\n{quote}"
        )
