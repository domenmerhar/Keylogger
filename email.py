import smtplib
from email.mime.text import MIMEText

# Define your email parameters
sender = 'your_email_address'
password = 'your_email_password'
recipient = 'recipient_email_address'
subject = "Keylogger"
message = 'Body of your email'

# Create a MIMEText object with your message
msg = MIMEText(message)

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
