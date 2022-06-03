import os
from selenium import webdriver
os.chdir('.\Ch13-Working_with_excel_spreadsheet')
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(firefox_profile=firefox_profile)
browser.get('https://www.billboard.com/charts/hot-100')
songElem = []
singerElem = []
for i in range(1, 110):
    if not i % 11 == 0:
        songElem.append((browser.find_element_by_xpath(
            '/html/body/main/div/div/div[7]/div/ol/li[{}]/button/span[2]/span[1]'.format(i))).text)
for i in range(1, 110):
    if not i % 11 == 0:
        singerElem.append((browser.find_element_by_xpath(
            '/html/body/main/div/div/div[7]/div/ol/li[{}]/button/span[2]/span[2]'.format(i))).text)
file = open('songs.txt', 'w')
file.write('\n'.join(songElem))
file.close()
file = open('singers.txt', 'w')
file.write('\n'.join(singerElem))
file.close()
