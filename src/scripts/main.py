from PIL import Image
import numpy as np
import pickle
import cv2
import sys
from doctest import OutputChecker
from steganography import encode
from convert_to_binary import str_to_binary
from paillier import Encrypt, Decrypt, generate_keys,image_encryption,show_encrypted_image
import os

image_path=sys.argv[1] #response from node js server
folder=image_path.split("/")
f_name=folder.pop()
type=f_name.split(".")[1]
n=len(folder)                  
folder_path="/".join(folder)

if(len(sys.argv)==3): #if the file type is not an image file we will embed it into one
	file_path=sys.argv[2] #response from node js server
	file=open(file_path,'r')
	str_to_conv=file.read()
	bin_result=str_to_binary(str_to_conv)
	encode(image_path,bin_result,folder_path) #saves an image file named "encoded_image.png" which is our stego file


publickey, privatekey = generate_keys()

im = Image.open(image_path)

encrypt_image = image_encryption(publickey,im)

encrypt_image.shape

enc_img=show_encrypted_image(encrypt_image,folder_path)

import matplotlib.pyplot as plt
img = plt.imread(folder_path+"/encrypted_image.png")
print(folder_path+"/encrypted_img.png")
gray = np.mean(img, axis=-1)

threshold = 0.5
binary = (gray > threshold).astype(np.uint8) * 1

img_array = np.array(binary)
os.remove(folder_path+"/encoded_image.png")