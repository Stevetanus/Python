import time
import pyautogui
wh = pyautogui.size()
wh
wh[0]
wh.width
wh[1]
wh.height
# move the mouse
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(10):
    pyautogui.move(100, 0, duration=0.25)
    pyautogui.move(0, 100, duration=0.25)
    pyautogui.move(-100, 0, duration=0.25)
    pyautogui.move(0, -100, duration=0.25)

pyautogui.position()
p = pyautogui.position()
p[1]
# click
pyautogui.click(50, 100)
p = pyautogui.position()
pyautogui.click(p)

time.sleep(5)
pyautogui.scroll(-200)
# mouse information
pyautogui.mouseInfo()
# screenshot
im = pyautogui.screenshot()
pyautogui.pixel(50, 100)
pyautogui.pixelMatchesColor(50, 100, (128, 203, 196))

b = pyautogui.locateOnScreen('python.png')
b
pyautogui.click(b)
pyautogui.click('python.png')
# window
fw = pyautogui.getActiveWindow()
fw
str(fw)
fw.width
fw.topleft
fw.width = 1000
fw.topleft = (800, 400)
fw.isMaximized
fw.isActive
fw.minimize()
time.sleep(5)
fw.activate()
fw.maximize()
pyautogui.getAllTitles()

pyautogui.getAllTitles()
