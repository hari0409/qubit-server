from PIL import Image
import numpy as np
import pickle
import cv2
import sys
from doctest import OutputChecker
from steganography import encode
from convert_to_binary import str_to_binary
from paillier import Encrypt, Decrypt, generate_keys,image_encryption,show_encrypted_image

file_path=sys.argv[1] #response from node js server
folder=file_path.split("\\")
f_name=folder.pop()
type=f_name.split(".")[1]
print(folder)                  
n=len(folder)                  
folder_path="\\".join(folder)

"""file=open(file_path,'r')
str_to_conv=file.read()
print(str_to_conv)

bin_result=str_to_binary(str_to_conv)
print(bin_result)


if(type!="png" or type!="jpg" or type!="jpeg"): #if the file type is not an image file we will embed it into one
	image_path="stego.jpg" #response from node js server
	encode(image_path,bin_result,folder_path) #saves an image file named "encoded_image.png" which is our stego file
"""

publickey, privatekey = generate_keys()
print(publickey.__repr__())

im = Image.open(folder_path+"\\encoded_image.png")
im.show()

encrypt_image = image_encryption(publickey,im)

encrypt_image.shape

enc_img=show_encrypted_image(encrypt_image,folder_path)

import matplotlib.pyplot as plt

img = plt.imread(folder_path+"\\encrypted_image.png")
gray = np.mean(img, axis=-1)

threshold = 0.5
binary = (gray > threshold).astype(np.uint8) * 1

img_array = np.array(binary)
print(img_array)

print(img_array.shape)