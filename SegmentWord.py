""" TO DO
1.WORK ON Y_HISTOGRAM -REMOVING ZEROES -- DONE
2.GENERALIZE THE COUNTLIMIT IN SEGMENTATION 
3.ONE HISTOGRAM WITH AXIS
4.VARIABLE NAMING ULLTA PULTA (JUMBLING) X AND Y HISTOGRAM...
5.HOW IS MIN MAX USED FOR SLICING ON LINE  118

"""

import cv2 as cv
from PIL import Image
import matplotlib.pyplot as mt
import numpy as np
def histogram_X(img):
       np_img=np.array(img)
       hist =np_img.sum(axis=1)/255
       return hist
def histogram_Y(img):
    np_img=np.array(img)
    hist =np_img.sum(axis=0)/255
    return hist
def cropParam(img_hist):
    for i in range(200):
        if img_hist[i]>0:
            minc=i
            break
    for j in reversed(range(200)):
        if img_hist[j]>0:
            maxc=j+1
            break
    print (minc,maxc)
    return minc , maxc
img = cv.imread('Paani4.png')
#cv.imshow('image ',img)
#cv.waitKey(0)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
ret,thresh1 = cv.threshold(img_gray,127,255,cv.THRESH_BINARY_INV) #return threshold value and thresholded image
#print( "Thresholded image",thresh1)
# print ret
#cv.imshow('thresh1',thresh1)
#cv.waitKey(0)
# print "Dimensions are: ",thresh1.shape
y= histogram_Y(thresh1)
#print(x)
# print x
x=histogram_X(thresh1)

#print (x)
#print (y)
x_min,x_max=cropParam(y)
y_min,y_max=cropParam(x)

thresh1=thresh1[y_min:y_max,x_min:x_max]
#print(thresh1.shape)
#cv.imshow('thresh1',thresh1)
#cv.waitKey(0)
x_modified=histogram_X(thresh1)
y_modified=histogram_Y(thresh1)

#print (y_modified)
#print (x_modified)
mt.plot(range(x_modified.shape[0]),x_modified)
mt.axis([0,x_max-x_min+1,0,y_max-y_min+1])
mt.title("X historgram")
mt.xlabel("vertical columns of image")
mt.ylabel("Frequency of white pixels")
#mt.show()

min_segmenty=min(y_modified)
count=0
segment=[]
for i in range(y_modified.shape[0]):
     if y_modified[i]<=min_segmenty +1 and count<5:
         count=count+1
         if count==5:
             segment.append(i-2)
     if y_modified[i]>min_segmenty +1:
         count=0
segment.append(y_modified.shape[0])
print(segment)

imglist=[]
s=0
for i in range(len(segment)):
    splited_img=thresh1[:,s:segment[i]]
    #h,w=splited.shape
    #splited_img=cv.CreateMat(h,w,cv.CV_32FC3)
    imglist.append(splited_img)
    s=segment[i]+1
"""for i in range(len(imglist)):
   img = Image.fromarray(imglist[i])
   img.save("myImg"+str(i)+".png")
   img.show()"""

#seperate upper part with the individdual letter
   
separated_images=[]

for i in range(len(imglist)):
    h=histogram_X(imglist[i]) #histogram for all images
    print(h)
    print("this was")
    #print(x_h)
    m_h=max(h)
    m_p=0
    for m_p in range(len(h)):
        if h[i]==m_h:
            break
        
    j=m_p#start parsing beow and stop when the value is less the 1/3 of max value
    while j<len(h) and h[j]>(m_h/3):
        j+=1
    y_min=j-1
    j=m_p
    while j>=0 and h[j]>(m_h/3):
        j-=1
    y_max=j+1
    #ukar parameters 
    
    upper=imglist[i][y_min:,:]
    middle=imglist[i][:y_max+1,:]# this is temproary middle we have to cut this 
    separated_images.append(upper)
    separated_images.append(middle)
    """for k in range(upper.shape[0]):
        for j in range(upper.shape[1]):
            print(upper[k][j])
    print()
    for k in range(middle.shape[0]):
        for j in range(middle.shape[1]):
            print(middle[k][j])"""

for i in range(len(separated_images)):
   img = Image.fromarray(separated_images[i])
   img.show()
   
    
    
    


    
    
    


