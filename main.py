import smtplib
import datetime as dt
import random
import email_config


with open("quotes.txt") as quotes_data:
    quotes_list = quotes_data.readlines()

current_time = dt.datetime.now()
if current_time.weekday() == 5:
    daily_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:  # creating an object from smtplib class
        connection.starttls()  # makes the connection secure
        connection.login(user=email_config.my_email, password=email_config.password)
        connection.sendmail(
            from_addr=email_config.my_email,
            to_addrs=email_config.send_to,
            msg=f"Subject: Daily quote\n\n{daily_quote}."
        )




