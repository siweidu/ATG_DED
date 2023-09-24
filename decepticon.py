'''
Toolpath for Trumpf 

'''
# -*- coding: utf-8 -*-



import imgtoline
#import numpy as np
import cv2 as cv
import sys




# load the image
file = 'decepticon.png'
img = cv.imread(file)
lines = imgtoline.horilines(img, 50, 1, 0.5)
#print (lines)
original_stdout = sys.stdout

# print (lines.shape[0])

with open ('toolpath.txt', 'w') as f:
    sys.stdout = f
    for i in range(lines.shape[0]):
        print('G01 X '+ str(-1*lines[i,0,0])+ ' Y '+ str(lines[i,0,1]))
        print('TC_ACL(2)    ;LASER ON')
        print('G01 X '+ str(-1*lines[i,1,0])+ ' Y '+ str(lines[i,1,1]))
        print('TC_ACL(1)    ;LASER OFF')
    sys.stdout = original_stdout


