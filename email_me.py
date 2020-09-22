#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import getpass

def generate_email(sender, receiver, subject, body):
  """Generate email without attachment"""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message['Subject'] = subject
  message['From'] = sender
  message['To'] = receiver
  message.set_content(body)

  return message
  
def send_email(package):
  """Sends the email package to the configured SMTP server."""
  mail_server = smtplib.SMTP('smtp.server.com') #It could gmail, outlook or whatever email service you use.
  mail_server.starttls() 
  mail_server.login('sender@whatever.com', 'password') 
  mail_server.send_message(package)
  mail_server.quit()