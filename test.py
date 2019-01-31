import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import Message
from email.errors import MessageError

email_user = 'joshua.kinnear'
email_password = 'Mysp@ce41'
email_senders = 'joshua.kinnear12@outlook.com'


subject = 'Automated Test'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_senders
msg['Subject'] = subject

body = 'Here is the link you wanted.'\
       'https://www.rocketseed.com'
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the https://www.rocketseed.com you wanted.
    </p>
  </body>
</html>
"""
msg.attach(MIMEText(body,'plain', 'html'))

filename='/home/joshua/Desktop/rocketseed.png'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_senders,text)
server.quit()
