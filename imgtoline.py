'''
input a binary picture  

Arguments
- print height in mm,       default value 50 mm
- LMD single line width,    default value 1 mm
- Overlap,                  default value 50%

output a ndarray of horizontal lines coodinates in mm [[line start y,line start x],[line end y, line end x], ... ]
'''
# -*- coding: utf-8 -*-




import numpy as np
import cv2 as cv

def horilines(img, pheight=50, linewd=1, overlap=0.5):

    #set parameters
    # pheight = 50               # print image height, mm
    # linewd = 1                  # line width in mm
    # overlap = 0.5               # overlap 0.5=50%
    step = linewd*(1-overlap)   # increament in y to next line mm

    
    imgChannel = len(img.shape)
    if imgChannel > 2:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    ret, imgB = cv.threshold(img, 125, 255, cv.THRESH_BINARY) #white 255, black 0
    
    # height, width, in image
    height = imgB.shape[0]
    width = imgB.shape[1]

    DPI = height/pheight                    # image height in pixal / real print height in mm
    n = int(pheight/step)                   # number of print lines 

    ypix= np.linspace(0,height, num=n, endpoint=False).astype(int)  # ys pixal in image
    yprt=np.arange(0,pheight,step)                                  # ys mm in real print

    assert step * DPI >1, "photo resolution too low"    # pix in y for a step
    assert ypix.shape == yprt.shape, "ypix != yprt, rounding error"

    # Display the Binary Image
    '''
    ArithmeticErrorcv.imshow("Binary Image", imgB)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''



    isStart = True
    isLine = False
    pixLines = []     #lines pixals


    for y in range(n):
        for x in range(width):
            if isStart == True and imgB[ypix[y],x]==0:          # print 0, not print 255
                pStart=[x/DPI, yprt[y]]
                isStart = False
            elif isStart == False and imgB[ypix[y],x]==255:
                pEnd=[x/DPI, yprt[y]]
                isStart = True
                isLine = True
            elif isStart== False and x==width:          # x last point is 0
                pEnd=[x/DPI, yprt[y]]
                isStart = True
                isLine = True

            if isLine==True:
                pixLines.append([pStart,pEnd])
                isLine = False

    arrLines = np.array(pixLines)           # in mm, [[line start y,line start x],[line end y, line end x], ... ]
    retLines = np.around(arrLines,decimals=3)       # round to 3 decimal for Gcode program

    return retLines





'''
if __name__ == '__main__':
    main()
'''
