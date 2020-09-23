#!/usr/bin/env python3

import psutil, shutil
import socket
import email_me
import os, sys
from win10toast import ToastNotifier # win10tost notifier works only on Windows 10.
import schedule  
import time 



def health_check():
  n = ToastNotifier()

#Warning if CPU usage is over 80%.
  def cpu_check():
    cpu_usage = psutil.cpu_percent() 
    return cpu_usage < 80

  
#Warning if available disk space is lower than 20%.
  def disc_space_check():  
    disk_usage = shutil.disk_usage("/")
    disk_total = disk_usage.total
    disk_free = disk_usage.used
    threshold = disk_free / disk_total * 100
    return threshold > 20


#Warning if available memory is less than 500MB.
  def available_memory_check():
    available = psutil.virtual_memory().available
    available_in_MB = available / 1024 ** 2 #convert to MB
    return available_in_MB > 500

#Email to be sent with the specified alert.
  def email_warning(warning):
    sender = "sender@whatever.com"
    receiver = "receiver@whatever.com"
    subject = warning
    body = "Alert! Check Your System ASAP!"
    message = email_me.generate_email(sender, receiver, subject, body)
    email_me.send_email(message)

  if not cpu_check():
    n.show_toast("Warning!", "CPU Usage is greater than 80%!", duration = 10, icon_path = "C:/Users/user/Pictures/alarm.ico") 
    subject = 'Alert! - CPU Usage is greater than 80%!!'
    email_warning(subject)

  if not disc_space_check():
    n.show_toast("Warning!", "Available disk space is less than 20%!", duration = 10, icon_path = "C:/Users/user/Pictures/alarm.ico")
    subject = "Alert! - Available disk space is less than 20%"
    email_warning(subject)

  if not available_memory_check():
    n.show_toast("Warning!", "Available memory is less than 500MB!", duration = 10, icon_path = "C:/Users/user/Pictures/alarm.ico")
    subject = "Alert! - Available memory is less than 500MB!"
    email_warning(subject)

schedule.every(1).minutes.do(health_check) # The script will be executed every minute with 1 second sleep.
while True:
    schedule.run_pending()
    time.sleep(1)

