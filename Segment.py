#from keras.preprocessing import image
from datetime import datetime
import uuid
import random
from keras_preprocessing import image
from Grabcut import Grabcut

#test_image=image.load_img('p9(7).png',target_size=(150,150),color_mode='grayscale')
path='p9(7).png'

import numpy as np
import cv2
from os import listdir,walk
from matplotlib import pyplot as plt


#img = cv2.imread('Operation3/Good/1.jpg')
#img=cv2.resize(img,(height,width))


def Segment(path,newpath):

    for file in listdir(path):
        #if not file.endswith(".ppm") or not file.endswith(".jpeg") or not file.endswith(".jpg") or not file.endswith(".png"):
         #   continue
        num = random.randint(1, 10000003)
        path1=path+file
        #print(path1)
        #USING THRESHOLD
        #RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=cv2.imread(path1)
        #img=Grabcut(img)
        img=cv2.resize(img,(200,200))
        #cv2.imshow("Image",img)
        #cv2.waitKey()
        #RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #gray = cv2.cvtColor(RGB,cv2.COLOR_RGB2HSV)
        blur=cv2.GaussianBlur(gray,(5,5),0)
        ret, thresh = cv2.threshold(blur,70,225,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        #cv2.imshow("Image",thresh)
        #cv2.waitKey()
        outfile = '%s%s.jpg'%(newpath,"ZNew"+ str(num))
        #print(outfile)
        cv2.imwrite(outfile,thresh)

def ImgSegment(path):
    img = cv2.imread(path)
    # img=cv2.resize(img,(200,200))
    # cv2.imshow("Image",img)
    # cv2.waitKey()
    # RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(RGB,cv2.COLOR_RGB2HSV)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # cv2.imshow("Image",img)
    # cv2.waitKey()
    cv2.imwrite("Threshinput.jpg", thresh)
    #outfile = '%s%s.jpg' % (newpath, "ZNew" + str(num))
    #print(outfile)
    #cv2.imwrite(outfile, thresh)



    #plt.imshow(RGB)
    #cv2.imshow('Original',img)
    #cv2.imshow('gray',gray)
    #cv2.imshow('blur',blur)
    #cv2.imshow('thresh',thresh)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



#ImgSegment(path)
#plt.imshow(img)
#plt.colorbar()
#plt.show()
'''
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float32)
fgdModel = np.zeros((1,65),np.float32)

rect = (height,width,50,50)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

'''
