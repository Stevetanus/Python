import pyautogui
import time
counts = 10
while counts > 0:
    time.sleep(2)
    print(f'{counts} to move')
    time.sleep(1)
    pyautogui.move(100, 0, duration=0.15)
    counts -= 1
