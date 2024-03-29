                                # IMAGE COMPRESSION 

import cv2
import numpy as np
import math
from zigzag import *
from RLE import *

block_size = 8

QUANTIZATION_MAT = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
])

img = cv2.imread('harry.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
  print("Image not loaded")
else:
  print("Image Loaded successfully")
  [h,w] = img.shape 

nbh = math.ceil(float(h)/block_size)
nbh = int(nbh)

nbw = math.ceil(float(w)/block_size)
nbw = int(nbw)

H =  block_size * nbh

W =  block_size * nbw
padded_img = np.zeros((H,W))
stream = ""
for i in range(int(h)):
        for j in range(int(w)):
                padded_img[i,j] = img[i,j]
                stream = stream + str(img[i,j])+" "

file = open("ACTUAL_IMAGE.txt","w")
file.write(stream)
file.close()
cv2.imwrite('UNCOMPRESSED_IMAGE.jpg', np.uint8(padded_img))

for i in range(nbh):
        row_start = i*block_size
        row_end = row_start+block_size
        for j in range(nbw):
            col_start = j*block_size
            col_end = col_start+block_size
            block = padded_img[ row_start : row_end , col_start : col_end ]
            DCT = cv2.dct(block)
            DCT_normalized = np.divide(DCT,QUANTIZATION_MAT).astype(int)
            reordered = zigzag(DCT_normalized)
            reshaped= np.reshape(reordered, (block_size, block_size))
            padded_img[row_start : row_end , col_start : col_end] = reshaped

cv2.imshow('encoded image', np.uint8(padded_img))
arranged = padded_img.flatten()
bitstream = get_run_length_encoding(arranged)
bitstream = str(padded_img.shape[0]) + " " + str(padded_img.shape[1]) + " " + bitstream + ";"
file1 = open("ENCODED_IMAGE.txt","w")
file1.write(bitstream)
file1.close()
cv2.waitKey(0)
cv2.destroyAllWindows()