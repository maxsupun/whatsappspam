import pyautogui
import time

f=open("script",'r')

time.sleep(10)

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")
