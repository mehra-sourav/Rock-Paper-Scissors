import cv2
import numpy as np

file='Operation3/Captures/Capture5.jpg'
cap=cv2.VideoCapture(0)
#vid=cv2.VideoWriter_fourcc(*'XVID')
#out=cv2.VideoWriter('output.avi',vid,20.0,(200,200))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #r=cv2.selectROI("ROI",gray,False,False)
    #r=cv2.selectROI(gray)

 #   out.write(gray)
    cv2.imshow('Video',gray)

    if cv2.waitKey(1) & 0xFF==ord('q'):
       break

    #elif cv2.waitKey(1) & 0xFF==ord('c'):
    cv2.imwrite(file,frame)

cap.release()
#out.release()
cv2.destroyAllWindows()
