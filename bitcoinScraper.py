import requests
from bs4 import BeautifulSoup
import smtplib, ssl


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}

def check_price():
    URL = input("Please enter the url of the product: ")
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find("span", "currency-price")
    growth = soup.find("span", "currency-percent-change currency-up")

    print(price)
    print(growth)

def send_mail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "xxxxxxxxxxxxx"  # Enter your address
    receiver_email = "xxxxxxxxxxxxxxx"  # Enter receiver address
    password = "xxxxxxxxxxx"
    message = "Go buy BitCoin"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
check_price()
