import pyperclip
import pyautogui
fw = pyautogui.getWindowsWithTitle('Notepad')[0]
fw.minimize()
fw.maximize()
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
vwindow = pyautogui.getWindowsWithTitle('Visual Studio Code')[0]
vwindow.minimize()
vwindow.maximize()
file = open('test.txt', 'w')
file.write(pyperclip.paste())
file.close()
