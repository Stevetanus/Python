import pyautogui
import time
import pyperclip
facebook = pyautogui.getWindowsWithTitle('facebook')[0]
facebook.minimize()
facebook.maximize()
# pyautogui.click('fb.png')
# pyautogui.mouseInfo()
pyautogui.click(1676, 196)
pyautogui.click(1491, 368)
pyautogui.write('lee')
time.sleep(4)
pyautogui.click(1434, 447)
pyautogui.typewrite(['enter'])
pyautogui.hotkey('ctrl', 'v')
pyautogui.typewrite(['enter'])
time.sleep(2)
pyautogui.write('Your breakfast today cost ')
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
pyautogui.write('3.00')
time.sleep(2)
pyautogui.typewrite(['enter'])
