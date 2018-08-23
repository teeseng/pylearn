# Seam-carving but in python

import cv2
import numpy as np
import math

mat = cv2.imread('lena.jpg', 0)
gradX = cv2.Sobel(mat, cv2.CV_64F, 1,0,ksize=3)
gradY = cv2.Sobel(mat, cv2.CV_64F, 0,1,ksize=3)
E = [ [0 for x in range(len(gradX))] for y in range(len(gradX[0])) ]

print(len(gradX))
print(len(gradX[0]))

for i in range(0,len(E) - 1):
    for j in range(0,len(E[0]) - 1):
        E[i][j] = math.sqrt((gradX[j][i] ** 2) + (gradY[j][i] ** 2)) 

M = [ [0 for x in range(len(gradX))] for y in range(len(gradX[0])) ]

print(M[1:3])
# need to do the dp here afterwards

