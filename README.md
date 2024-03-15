# jpeg-image-compression
this project is based on the compressing using Discrete Cosine Transform and runlength encoding.

i have given the requirements in the requirements.txt, the project consist of three files

encoding_image.py : applying DCT to image and performing run length encoding after that.

decoding_image.py : applying the same  in reverse order.

zigzag.py : this is used while perfomring RLE(run length encoding)

this is lossy compression as while performing Quantization step some data is lossed which cannot be retrived in the reverse step.

zigzag.py has been taken from: <a href = "https://github.com/amzhang1/simple-JPEG-compression">https://github.com/amzhang1/simple-JPEG-compression</a>
