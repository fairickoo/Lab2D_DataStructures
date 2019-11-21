import cv2 
import serial
import time
#import os

# path 
path_original = r'C:/out/4.bmp'
path_crop=r'C:/image/crop/test.png'
path_BW=r'C:/image/b-w/bw .png'
path_RZ= r'C:/image/crop/resize/h.png'

#cv2.imshow('image original', img)
arduino = serial.Serial('COM1',115200)   
print(arduino.name)
arduino.write(b'r')
arduino.write(b'm')
arduino.write(b'l')
arduino.write(b'c')
"""while(True):
    if(arduino.inWaiting()):
        raw = arduino.readline()
        data = raw.decode('ascii')
        print(data)"""
arduino.close()

def Crop(x,y,h,w,path,pathsave) :
    img = cv2.imread(path, 0) 
    crop = img[y:y+h, x:x+w]
    #cv2.imshow('Image crop',crop)
    cv2.imwrite(pathsave, crop)

def Black_White(path,pathsaveBW):
    img_grey = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    thresh = 64
    img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow('Image crop',img_binary)
    cv2.imwrite(pathsaveBW, img_binary)

def getValue_pixel(path):
    imV = cv2.imread(path, 0) 
    p = imV.shape
    rows,cols = imV.shape
    for y in range(rows):
        for x in range(cols):
            if imV[y,x]==255:
                imV[y,x]=1
            print(imV[y,x], end = '')
        print("\t")
    
    if ((imV[0][0]==0 and imV[1][1]==0 and imV[2][2]==0 and imV[3][3]==0 and imV[1][0]==0 
    and imV[2][0]==0 and imV[2][1]==0 and imV[3][0]==0 and imV[3][1]==0 and imV[3][2]==0 ) 
    or ( imV[1][0]==0  and imV[2][0]==0 and imV[2][1]==0 and imV[3][0]==0 and imV[3][1]==0 and imV[3][2]==0 and imV[2][2]==1 ) 
    or (imV[2][0]==0 and imV[3][1]==0 and imV[3][0]==0 and imV[2][1]==1)):
        print('lower')
    elif ((imV[0][0]==0 and imV[1][1]==0 and imV[2][2]==0 and imV[3][3]==0 and imV[0][1]==0 
    and imV[0][2]==0 and imV[0][3]==0 and imV[1][2]==0 and imV[1][3]==0 and imV[2][3]==0 ) 
    or ( imV[0][1]==0  and imV[0][2]==0 and imV[0][3]==0 and imV[1][2]==0 and imV[1][3]==0 and imV[2][3]==0 and imV[1][1]==1) 
    or (imV[0][2]==0 and imV[0][3]==0 and imV[1][3]==0 and imV[1][2]==1)):
        print('upper')
    elif ((imV[0][0]==0 and imV[1][0]==0 and imV[2][0]==0 and imV[3][0]==0 )
    or (imV[0][0]==0 and imV[1][0]==0 and imV[2][0]==0 and imV[3][0]==0 
    and imV[0][1]==0 and imV[1][1]==0 and imV[2][1]==0 and imV[3][1]==0 ) 
    or (imV[1][0]==0 and imV[2][0]==0 and imV[3][0]==0 )) :
        print('left')
    elif ((imV[0][2]==0 and imV[1][2]==0 and imV[2][2]==0 and imV[3][2]==0 
    and imV[0][3]==0 and imV[1][3]==0 and imV[2][3]==0 and imV[3][3]==0  )
    or (imV[0][3]==0 and imV[1][3]==0 and imV[2][3]==0 and imV[3][3]==0) 
    or (imV[1][3]==0 and imV[2][3]==0 and imV[3][3]==0 )) :
        print('right')
    elif ((imV[0][0]==0 and imV[0][1]==0 and imV[0][2]==0 and imV[0][3]==0 
    and imV[1][0]==0 and imV[1][1]==0 and imV[1][2]==0 and imV[1][3]==0 )
    or (imV[0][0]==0 and imV[0][1]==0 and imV[0][2]==0 and imV[0][3]==0)): 
        print('top')
    elif ((imV[2][0]==0 and imV[2][1]==0 and imV[2][2]==0 and imV[2][3]==0 
    and imV[3][0]==0 and imV[3][1]==0 and imV[3][2]==0 and imV[3][3]==0 )
    or (imV[3][0]==0 and imV[3][1]==0 and imV[3][2]==0 and imV[3][3]==0)): 
        print('bottom')    
    print('W H :',p)
    #cv2.imshow('Imagefor get value =',imgV)

def Resize(path,pathsave):
    img_Trans = cv2.imread(path,0)
    W = 4
    shape=img_Trans.shape
    height, width = shape
    imgScale = W/width
    newX,newY = img_Trans.shape[1]*imgScale, img_Trans.shape[0]*imgScale
    newimg = cv2.resize(img_Trans,(int(newX),int(newY)))
    #cv2.imshow("Show by CV2",newimg)
    cv2.imwrite(pathsave, newimg)


#-------------------------------------------------------------
#main 
x=60
y=80
h=160
w=160
Black_White(path_original,path_BW)
Crop(x,y,h,w,path_BW,path_crop)
Resize(path_crop,path_RZ)
getValue_pixel(path_RZ)
cv2.waitKey(0)
cv2.destroyAllWindows()