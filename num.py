__author__ = 'wangli17562'
import cv2
from cv2 import  cv
import numpy as np
import scipy as sp

#def cutleft(src,)
image = cv2.imread("simple.jpg")
w_pos=[]
h_pos=[]
cv2.threshold(image,100 , 255, 0,image)
m,n=image.shape[:2]
for x in range(0,n):
    for y in range(0,m):
        image[y,x]=255-image[y,x]

x_flag=0
y_flag=0
pre_x_flag=x_flag
pre_y_flag=y_flag
for x in range(0,n):
    count=0
    pre_x_flag=x_flag
    for y in range(0,m):
        count+=image[y,x]
    if count[0] > 0:
        x_flag=1
    else:
        x_flag=0
    if pre_x_flag!=x_flag:
        w_pos.append(x)

leng=w_pos.__len__()
for i in range(0,leng/2):
    for y in range(0,m):
        count=0
        for x in range(w_pos[2*i],w_pos[2*i+1]):
            count+=image[y,x][0]
        pre_y_flag=y_flag
        if count>0:
            y_flag=1
        else:
            y_flag=0
        if pre_y_flag!=y_flag:
            h_pos.append(y)

match_img=[]
tmp_mg=[]

for i in range(0,leng/2):
    cv2.waitKey(3)
    cv2.rectangle(image,(w_pos[i],h_pos[i]),(w_pos[i+1],h_pos[i+1]),(255,255,0))
    imgIP=cv.GetImage(cv.fromarray(image))
    cv.SetImageROI(imgIP,(w_pos[2*i],h_pos[2*i],w_pos[2*i+1]-w_pos[2*i],h_pos[2*i+1]-h_pos[2*i]))
    img_cache=cv.CreateImage((w_pos[2*i+1]-w_pos[2*i],h_pos[2*i+1]-h_pos[2*i]),cv.IPL_DEPTH_8U,3)
    cv.Copy(imgIP,img_cache)
    match_img.append(img_cache)
#    cv.SaveImage('ss'+bytes(i)+'.jpg',match_img[i])
    cv.ResetImageROI(imgIP)
#    cv.ShowImage('window'+bytes(i),match_img[i])

#aa=image.copy((range(10,20),range(20,100)))
#cv2.imshow("hello",aa)
#cv2.imshow("img",image)
print w_pos
print h_pos
cv2.waitKey(0)

