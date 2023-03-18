import smtplib
from  email.message import EmailMessage
msg=EmailMessage()
msg['subject']='subject mail'
msg['to']='nnnnnnnnn@gamil'
msg['From']='norhank527@gmail.com'
msg.set_content('body')

with smtplib.SMTP('sssssssss@gamil.com',587) as smtp:
    smtp.starttls()
    smtp.login('norhank527@gmail.com')
    smtp.send_message(msg)
