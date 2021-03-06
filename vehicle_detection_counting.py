# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

cascade_src = 'cars3.xml'
video_src = '1.mp4'
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
while True:

    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.2,5 )
    i= 0
    for (x,y,w,h) in cars:
        i=i+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,i*50),2)
    
    cv2.imshow('video', img)
    print( "Found "+str(len(cars))+" car(s)")
    b=str(len(cars))
    a= float(b)
    if a>=5:
        print ("more traffic")
    else:
        print ("no traffic")    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
