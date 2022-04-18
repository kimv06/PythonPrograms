import random
import pyautogui as pg
import time
animal=('dog','cat','buffalow','donkey','animal','horse','elephant')
time.sleep(10)
for i in range(25):
    a=random.choice(animal)
    pg.write('you are a '+ a)
    pg.press('enter')