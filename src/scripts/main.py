from PIL import Image
import numpy as np
import pickle
import sys
from doctest import OutputChecker
from steganography import encode
from convert_to_binary import str_to_binary
from paillier import Encrypt, Decrypt, generate_keys,image_encryption,show_encrypted_image,image_decryption,show_decrypted_image
from qkd import gen_bases,encode_message

image_path=sys.argv[1] #response from node js server
folder=image_path.split("/")
f_name=folder.pop()
type=f_name.split(".")[1]
print(folder)                  
n=len(folder)                  
folder_path="/".join(folder)
print(folder_path)

if(len(sys.argv)==3): #if the file type is not an image file we will embed it into one
	file_path=sys.argv[2] #response from node js server
	file=open(file_path,'r')
	str_to_conv=file.read()
	print(str_to_conv)

	bin_result=str_to_binary(str_to_conv)
	print(bin_result)

	encode(image_path,bin_result,folder_path) #saves an image file named "encoded_image.png" which is our stego file


publickey, privatekey = generate_keys()
print(publickey._repr_())

im = Image.open(image_path)
im.show()

encrypt_image = image_encryption(publickey,im)

encrypt_image.shape

enc_img=show_encrypted_image(encrypt_image,folder_path,f_name)

import matplotlib.pyplot as plt
img = plt.imread(folder_path+"/encrypted_"+f_name)
#from paillier import increase_brightness

#output=increase_brightness(publickey, img, 1)

gray = np.mean(img, axis=-1)

threshold = 0.5
binary = (gray > threshold).astype(np.uint8) * 1

img_array = np.array(binary)
print(img_array)

print(img_array.shape)

key_size=img_array.shape[1]
# bases=gen_bases(key_size)
# encr=encode_message(img_array,bases,img_array.shape[0],key_size)
# print(encr)