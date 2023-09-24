'''
#import rasterio


#dataset = rasterio.open('SGTopo/output_SRTMGL1.tif')

#band1 = dataset.read(1)
#cv2.imwrite('SGTopo_Gray.tif', band1)


'''
import cv2
import numpy as np
import sys
import imgtoline


img = cv2.imread('SGTopo_Gray.tif')
imgG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img.max()


LayerHeight = 0.5
layer = 0
original_stdout = sys.stdout
f = open("toolpath.txt", "w")
sys.stdout = f

for z in np.arange(0,imgG.max(),20):
    ret, imgB = cv2.threshold(imgG, z, 255, cv2.THRESH_BINARY_INV) #white 255, black 0
    file = 'SGtopo'+str(layer)+'.tif'
    cv2.imwrite(file,imgB)
    
    lines = imgtoline.horilines(imgB, 70, 1, 0.5)
    
    for i in range(lines.shape[0]):
        print('G01 X '+ str(-1*lines[i,0,0])+ ' Y '+ str(lines[i,0,1]) + ' Z '+str(np.around(layer*LayerHeight,decimals=3)))
        print('TC_ACL(2)    ;LASER ON')
        print('G01 X '+ str(-1*lines[i,1,0])+ ' Y '+ str(lines[i,1,1]) + ' Z '+str(np.around(layer*LayerHeight,decimals=3)))
        print('TC_ACL(1)    ;LASER OFF')
        
    layer+=1
f.close()




sys.stdout = original_stdout


data0 = data1 = data2 = ""

with open('LMD_ATG_tempHead.txt') as fHead:
    data0 = fHead.read()

with open('toolpath.txt') as fToolpath:
    data1 = fToolpath.read()

with open('LMD_ATG_tempEnd.txt') as fEnd:
    data2 = fEnd.read()


data0 += "\n"
data0 += data1
data0 += "\n"
data0 += data2


with open('LMD_ATG_SGtopo.HP', 'w') as fATG:
    fATG.write(data0)



fHead.close()
fToolpath.close()
fEnd.close()
fATG.close()


