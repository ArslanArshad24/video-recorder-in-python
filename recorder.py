from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name= f"{time_stamp}.mp4"
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter(file_name,fourcc,20.0, (width,height))
# print(time_stamp)

webcam = cv2.VideoCapture(0)
while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_fine = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Capture',img_fine)
    
    _,frame=webcam.read()
    frame_h, frame_w,_ = frame.shape
    # cv2.imshow('webcam',frame)
    
    img_fine[0:frame_h,0:frame_w,:] = frame[0:frame_h,0:frame_w,:]
    
    captured_video.write(img_fine)
    
    
    if cv2.waitKey(10) == ord('q'):
        break

