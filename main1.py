import pyautogui
import uuid
import time

while True:
    s = uuid.uuid4()
    file = open(f'{str(s)}.txt', 'w')
    file.write(s)
    file.close()


    # pyautogui.typewrite('hello')

    # pyautogui.press('enter')
    
   