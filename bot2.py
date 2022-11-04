import smtplib
import ssl
import imghdr

from email.message import EmailMessage



email_sender = #masukkan  email pengirim
email_password = #masukkan pw email pengirim
list_email = [#masukkan list email yang dituju  
    ]

subject = 'lorem ipsum'
body = """
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus aspernatur nam ab odio ducimus ratione ad ipsa similique, recusandae a, atque nihil blanditiis eveniet quam debitis tempora officia fuga. Sint!
"""

em = EmailMessage()
em['From'] = email_sender
em['Subject'] = subject
em.set_content(body)

with open('wedus.jpeg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name
em.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, list_email, em.as_string())
