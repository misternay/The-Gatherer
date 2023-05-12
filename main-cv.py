import cv2 as cv
import pyautogui as pa
from time import sleep
from imagetool import ImageTool
from window_capture import WindowCapture
from time import time
import numpy as np
from pynput.mouse import Button, Controller
from bot_thread import *

x, y, w, h = 900, 620, 200, 200

loop_time = time()
mouse = Controller()

while True:
    sleep(1)
    wincap = WindowCapture(None)
    print('Start.')
    # debug the loop rate
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    im = ImageTool()
    cv.imwrite("images/sample.PNG", wincap.get_screenshot())
    # pa.screenshot("images/sample.PNG", (x, y, w, h))
    image = cv.imread("images/sample.PNG")
    chernust = cv.imread("images/chernust.PNG")
    mobbar1 = im.imageSearch(image="images/chernust.png")
    # mobbar2 =  im.imageSearch(image="gloriavictor/imgs/mini/pull-down.PNG")
    # mobbar3 =  im.imageSearch(image="gloriavictor/imgs/mini/pull-left.PNG")
    # mobbar4 =  im.imageSearch(image="gloriavictor/imgs/mini/pull-right.PNG")
    # mobBars = [mobbar1, mobbar2, mobbar3, mobbar4]
    mobBars = [mobbar1]
    for mobBar in mobBars:
        print(mobBar)
        if mobBar[0][0] != -1:
            print("found", mobBar)
            # pa.moveTo(mobBar[0][0],mobBar[0][1],duration=0.5)
            mouse.position = (mobBar[0][0], mobBar[0][1])

            print("click")
			#Action 2 (Movement click)
            # pa.click(button="left")
            mouse.click(Button.left)
            sleep(10)
    else:
        print('Needle not found.')