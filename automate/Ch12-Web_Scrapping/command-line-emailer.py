#! python3
# commandLineEmailer.py - Takes an email address and string,
# then emails string to the address.
# Designed to be used with Gmail.
# Be sure to enable Keyboard Commands in Gmail Settings.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import sys

# insert origin email address and password here

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

# driver = webdriver.Firefox(firefox_profile=firefox_profile)
if len(sys.argv) > 1:

    emailTo = sys.argv[1]

    # passes all arguments past address as the message

    if len(sys.argv) > 2:

        messageText = ' '.join(sys.argv[2:])

    else:

        messageText = sys.argv[2]

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    browser.get('https://mail.google.com')

    # insert email address and wait for next page to load
    emailFrom = input('enter your own email address')
    userElem = browser.find_element_by_name('identifier')
    userElem.send_keys(emailFrom)
    userElem.send_keys(Keys.ENTER)

    input('Press ENTER once the password page has finished loading.')

    # insert password and wait for next page to load
    password = getpass.getpass()
    passElem = browser.find_element_by_name('password')
    passElem.send_keys(password)
    passElem.send_keys(Keys.ENTER)

    input('Press ENTER once the inbox page has finished loading.')

    # open new message window and wait to proceed

    htmlElem = browser.find_element_by_class_name('T-I-KE')
    htmlElem.click()

    input('Press ENTER once the new message box has finished loading.')
    subject = 'You have a new message from ' + emailFrom

    recipientElem = browser.find_element_by_name('to')
    recipientElem.send_keys(emailTo)

    subjectElem = browser.find_element_by_name('subjectbox')
    subjectElem.send_keys(subject)

    messElem = browser.find_element_by_class_name('editable')
    messElem.send_keys(messageText)

    input('Press ENTER once the new message has been input.')

    sendElem = browser.find_element_by_class_name('v7')
    sendElem.send_keys(Keys.ENTER)

else:

    print('Include who you want to send to, ' +
          'followed by a message in the argument.')

browser.quit()
exit
