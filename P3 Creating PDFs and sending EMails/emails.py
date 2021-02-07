#!/usr/bin/env python3


import mimetypes
import os.path
import smtplib
import getpass
from email.message import EmailMessage

def generate(sender, recipient, subject, body, attachment_path):
	message = EmailMessage()
	message['From']=sender
	message['To']= recipient
	message['Subject']=subject
	message.set_content(body)
	mime_type, _ =mimetypes.guess_type(attachment_path)
	mime_type, mime_subtype = mime_type.split('/',1)
	with open(attachment_path, 'rb') as a:
		message.add_attachment(a.read(),
			maintype=mime_type,
			subtype=mime_subtype,
			filename=os.path.basename(attachment_path))
	return message

def send(message):
	server=smtplib.SMTP_SSL('smtp.gmail.com')
	username= "asteroidbyjava007@gmail.com"
	passw= getpass.getpass("Password? :")
	server.login(username, passw)
	server.send_message(message)
	server.quit()
