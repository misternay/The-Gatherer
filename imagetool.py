import string
import cv2 as cv2
import pyautogui as pa
from time import sleep
from python_imagesearch.imagesearch import imagesearch
import numpy as np
import os

class ImageTool:
    def imageSearch(self, image):
        img_rgb = cv2.imread("images/sample.PNG")
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(image, 0)
        if template is None:
            raise FileNotFoundError('Image file not found: {}'.format(image))
        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print("max_val", max_val)
        print("max_val", image)
        if max_val < 0.4:
            return [[-1, -1], image]
        return [max_loc, image]
    
    def imagesearch_from_folder(self, path):
        print(path)
        imagesPos = []
        path = path if path[-1] == '/' or '\\' else path+'/'
        print(path)
        valid_images = [".jpg", ".gif", ".png", ".jpeg"]
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and os.path.splitext(f)[1].lower() in valid_images]
        print(files)
        for file in files:
            pos = self.imageSearch(path+file)
            print(path+file)
            imagesPos.append(pos)
        return imagesPos