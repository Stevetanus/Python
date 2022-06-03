from selenium.webdriver.common.keys import Keys
import bs4
from selenium import webdriver
import requests
import webbrowser
webbrowser.open('http://inventwithpython.com/')
# 用requests.get()函式下載某個網頁
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
# 錯誤檢測
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
# 將下載的檔案儲存到硬碟
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
# wb作為第二引數，會以寫入二進位模式開啟檔案，目的是為了儲存該文字中的「Unicode」編碼。
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
# BeautifulSoup4 從html建立一個BeautifulSoup物件
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
noStarchSoup
# bs4 select()
exampleFile = open(
    'C:/Users/steve/Documents/GitHub/python-training/automate/Ch12-Web_Scrapping/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('.slogan')
type(elems)
len(elems)
type(elems[0])
str(elems[0])
elems[0].getText()
elems[0].attrs
# bs4 get()
soup = bs4.BeautifulSoup(open(
    'C:/Users/steve/Documents/GitHub/python-training/automate/Ch12-Web_Scrapping/example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs
# selenium module
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_tag_name('h1')
    print('Found first h1 tag, here is the text: <%s>' % (elem.text))
except:
    print('Was not able to find an element with that name.')
# 點按頁面
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()
# 填寫和提交表單
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('steven')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('123456')
passwordElem.submit()
# 傳送特殊按鍵
# browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.text
htmlElem.send_keys(Keys.END)    # scrolls to bottom
htmlElem.send_keys(Keys.HOME)   # scrolls to top
browser.back()
browser.quit()
