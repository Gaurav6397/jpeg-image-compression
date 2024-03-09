                        # RUN LENGTH ENCODING 
import numpy as np
def get_run_length_encoding(image):
    i = 0
    skip = 0
    bitstream = ""
    image = image.astype(int)
    while i < image.shape[0]:
        if image[i] != 0:
            bitstream = bitstream + str(image[i])+ " " +str(skip)+ " "
            skip = 0
        else:
            skip = skip + 1
        i = i + 1

    return bitstream