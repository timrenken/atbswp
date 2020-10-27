#! python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import logging,json,time,os

os.system("clear")

# Email credentials located in home directory
creds = json.loads(open(Path.home() / 'email_creds.json', 'r').read())
email = creds["email"]
pw = creds["pass"]

# Setting path for the Chrome Web Driver
PATH = "/usr/local/bin/chromedriver"

# Get inputs from the user
recipient = input("Send to: ")
subject = input("Subject: ")
print('\nBody: (include \\n for line breaks)')
body_message = input(">> ")

# Open the browser 
browser = webdriver.Chrome(PATH)
browser.get('http://mail.google.com/mail/h/')

# Enters email address
email_form = browser.find_element_by_name('identifier')
logging.debug(type(email_form))
email_form.send_keys(email)
email_form.send_keys(Keys.RETURN)
time.sleep(2)

# Enters the password
pass_form = browser.find_element_by_name('password')
pass_form.send_keys(pw)
pass_form.send_keys(Keys.RETURN)
time.sleep(3)

# Opens a new Email
compose_button = browser.find_element_by_link_text('Compose Mail')
compose_button.click()
time.sleep(5)

# Enters the reipient's email address
to_field = browser.find_element_by_id('to')
to_field.send_keys(recipient)

# Enters the subject
subject_field = browser.find_element_by_name('subject')
subject_field.send_keys(subject)


body_field = browser.find_element_by_name('body')
# Sets the cursor to the beginning of the body text field, before signature
body_field.click()
body_field.send_keys(Keys.ARROW_UP * 5)

# Enters the Body, and utilizes the \n
for line in body_message.split("\n"):
    body_field.send_keys(line)
    body_field.send_keys(Keys.RETURN)

# Hits the send button
send_button = browser.find_element_by_name('nvp_bu_send')
send_button.click()
time.sleep(2)

# Close the browserß
browser.close()