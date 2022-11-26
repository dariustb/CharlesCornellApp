# Python v. 3.10.4, 64-bit

import cv2      # Exracts frames from video
import PIL      

def extract_frames(video_path: str):
    ''' Extracts frames from video_path and saves them into ouptut folder'''
    # From fireant on StackOverflow
    # https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
    
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("output/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        count += 1
    print("Frames counted:", count)

def search_frames():
    pass

if __name__ == "__main__":
    video_path = "input/huh2.mp4"
    ref_image  = "input/ref.jpg"
    
    extract_frames(video_path)

import cv2
import numpy as np
from matplotlib import pyplot as plt

def process_image(img_rgb, template, count):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # This will write different res.png for each frame. Change this as you require
    cv2.imwrite('res{0}.png'.format(count),img_rgb)   


def main():
    vidcap = cv2.VideoCapture('My_Video.mp4')
    template = cv2.imread('small_icon_I_am_looking_for.png',0)  # open template only once
    count = 0
    while True:
      success,image = vidcap.read()
      if not success: break         # loop and a half construct is useful
      print ('Read a new frame: ', success)
      process_image(image, template, count)
      count += 1
