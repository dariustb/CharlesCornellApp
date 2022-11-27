# NOTE: This is the functions file,
# To run the program, go to main.py

''' Functions to be called and ran inside of the driver file, main.py'''

import cv2      # Exracts frames from video
from matplotlib import pyplot as plt
import numpy as np
    
def run(video_path: str, ref_path: str):
    ''' Extracts frames from video_path to get checked for the ref image'''
    # From fireant on StackOverflow
    # https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
    
    vidcap = cv2.VideoCapture(video_path)
    template = cv2.imread(ref_path, 0)
    count = 0

    while True:
        success,image = vidcap.read()
        if not success:
            break  
        process_image(image, template, count)

        count += 1
    print("Frames counted:", count)

def process_image(img_rgb, template, count):
    ''' Checks if the image matches the frame '''
    # From gowrath and georgiecasey on StackOverflow
    # https://stackoverflow.com/questions/41336746/find-an-image-inside-of-a-video-using-python

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    if len(loc[0]) > 0 :
        cv2.imwrite('output/img{0}_orig.png'.format(count),img_rgb)   
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('output/img{0}_lined.png'.format(count),img_rgb)   
