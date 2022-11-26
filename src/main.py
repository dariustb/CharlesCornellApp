# Python v. 3.10.4, 64-bit

# ------------------------------------------------
# This is to solve the challenge given by
# Charles Cornell for some free music instruction
# ------------------------------------------------

import cv2      # Exracts frames from video

def extractFrames(video_path: str):
    ''' Extracts frames from video_path and saves them into ouptut folder'''
    # From fireant on StackOverflow
    # https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
    
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("output/frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print("Count =", count)

def searchFrames():
    pass

if __name__ == "__main__":
    video_path = "input/skunky.mp4"
    
    extractFrames(video_path)