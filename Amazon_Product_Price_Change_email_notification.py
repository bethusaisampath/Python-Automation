import requests
import smtplib
from bs4 import BeautifulSoup

LINK="https://www.amazon.in/dp/B09V4D7459?th=1"

CUTOFF_PRICE = 100000

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

# Send a request to fetch HTML of the page.
response = requests.get(LINK, headers=header)

# Create a soup object
soup = BeautifulSoup(response.content, "lxml")

# Get the price of the item and converting the string amount to float.
price = (soup.find(name="span", class_="a-offscreen")).get_text()
#price = (soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")).get_text()
final_price = float((price[1:].replace(',', '')))

title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")

# Remove extra spaces in the title using strip()
title = title.get_text().strip("        ")

#enable this: https://www.google.com/settings/security/lesssecureapps
# Compare the current price of the item with the cutoff price.
# If there is a price drop, send an email.
if final_price < CUTOFF_PRICE:
    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user='sender_email', password='sender_email_password')
    connection.sendmail(from_addr='sender_email',
                        to_addrs='Receiver_email',
                        msg=f"Subject:Amazon Price Drop Alert! \n\n {title} is now available at Rs.{final_price}.\n Buy now! Link: {LINK}")
    connection.close()