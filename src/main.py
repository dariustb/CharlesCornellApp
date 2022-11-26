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