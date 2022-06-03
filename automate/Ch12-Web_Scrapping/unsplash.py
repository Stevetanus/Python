from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import sys
import os
import urllib.request
import time

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(firefox_profile=firefox_profile)
if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
    browser.get('https://unsplash.com/s/photos/{}'.format(search))
else:
    browser.get('https://unsplash.com')
    topics = []
    topicElem = browser.find_elements_by_class_name('qvEaq')
    for e in topicElem:
        topics.append(e.text)
    print(topics[2:-1])
    search = input(
        'Enter one of the topics above which you are interested in ~ ')
    search = search.lower()
    browser.get('https://unsplash.com/t/{}'.format(search))

os.makedirs(search, exist_ok=True)
print('making {} dir'.format(search))
picElem = browser.find_elements_by_class_name('oCCRx')
location = os.path.join(os.getcwd(), search)
try:
    for i in range(5):
        alt = picElem[i].get_attribute('alt')
        src = picElem[i].get_attribute('src')
        urllib.request.urlretrieve(src, '{}\\{}.png'.format(location, alt))
    print('photo download complete!')
except:
    print('error')
time.sleep(30)
browser.close()
exit
