import smtplib
from email.message import EmailMessage

# Settings
yourAdress = 'your email'
yourPassword = 'your password'
receiverEmail = 'receiver email'
subject = 'subject'
content = 'content'
smtp = 'your.smtp.com'
port = 111

# Sending
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = yourAdress
msg['To'] = receiverEmail

msg.set_content(content)

with smtplib.SMTP_SSL(smtp, port) as smtp:
    smtp.login(yourAdress, yourPassword)
    smtp.send_message(msg)