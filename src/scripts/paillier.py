import random
import numpy as np
import pandas as pd
from PIL import Image
import cv2
from doctest import OutputChecker

def lcm(a, b):

    return a * b // xgcd(a,b)[0]

def xgcd(a, b):

    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = xgcd(b % a, a)
        return (g, x - (b // a) * y, y)

def multiplicative_inverse(a, modulus):

    g, x, y = xgcd(a, modulus)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % modulus

def binary_exponent(base, exponent, modulus):

    if modulus == 1:
        yield 0
        return
    bitmask = 1 << exponent.bit_length() - 1
    res = 1
    while bitmask:
        res = (res * res) % modulus
        if bitmask & exponent:
            res = (res * base) % modulus
        yield res
        bitmask >>= 1

def is_probably_prime(n):
    """
    Check if n is prime or not

    """
    tests = max(128, n.bit_length())
    for i in range(tests):
        rand = random.randint(1,n-1)
        return 1 in binary_exponent(rand, n-1, n)

def generate_prime(bitlen=128):
    n = random.getrandbits(bitlen) | 1<<(bitlen-1) | 1
    while not is_probably_prime(n):
        n = random.getrandbits(bitlen) | 1<<(bitlen-1) | 1
    return n
    
class PrivateKey:
    def __init__(self, p, q, n):

        self.λ = lcm( p-1, q-1)
        self.μ = multiplicative_inverse( self.λ, n)

    def __repr__(self):
        return ("---\nPrivate Key :\nλ:\t"+str(self.λ) +"\nμ:\t"+str(self.μ) +"\n---")

class PublicKey:
    def __init__(self, n):
        self.n = n
        self.nsq = n * n
        self.g = n+1

    def __repr__(self):
        return ("---\nPublic Key :\nn:\t"+ str(self.n) +"\n---")

def generate_keys(bitlen=128):

    p = generate_prime(bitlen)
    q = generate_prime(bitlen)
    n = p * q
    return (PublicKey(n), PrivateKey(p, q, n))

def Encrypt(public_key, plaintext):
    r = random.randint( 1, public_key.n-1)
    while not xgcd( r, public_key.n)[0] == 1:
        r = random.randint( 1, public_key.n)

    a = pow(public_key.g, plaintext, public_key.nsq)
    b = pow(r, public_key.n, public_key.nsq)

    ciphertext = (a * b) % public_key.nsq
    return ciphertext

def Decrypt(public_key, private_key, ciphertext):
    x = pow(ciphertext, private_key.λ, public_key.nsq)
    L = lambda x: (x - 1) // public_key.n

    plaintext = (L(x) * private_key.μ) % public_key.n
    return plaintext

def homomorphic_add(public_key, a, b):
    return (a * b) % public_key.nsq


def homomorphic_add_constant(public_key, a, k):
    return a * pow( public_key.g, k, public_key.nsq) % public_key.nsq


def homomorphic_mult_constant(public_key, a, k):
    return pow(a, k, public_key.nsq)
    
def image_encryption(public_key, plain_image):

    cipher_image = np.asarray(plain_image)
    shape = cipher_image.shape
    cipher_image = cipher_image.flatten().tolist()
    cipher_image = [Encrypt(public_key, pix) for pix in cipher_image]

    return np.asarray(cipher_image).reshape(shape)


def image_decryption(public_key, private_key, cipher_image):

    shape = cipher_image.shape
    plain_image = cipher_image.flatten().tolist()
    plain_image = [Decrypt(public_key, private_key, pix) for pix in plain_image]
    plain_image = [pix if pix < 255 else 255 for pix in plain_image]
    plain_image = [pix if pix > 0 else 0 for pix in plain_image]

    return Image.fromarray(np.asarray(plain_image).reshape(shape).astype(np.uint8))


def increase_brightness(public_key, cipher_image, factor):

    shape = cipher_image.shape
    brightend_image = cipher_image.flatten().tolist()
    brightend_image = [homomorphic_add_constant(public_key, pix, factor) for pix in brightend_image]

    return np.asarray(brightend_image).reshape(shape)

def show_encrypted_image(cipher_image,folder_path):

    for i in range(0,cipher_image.shape[0]):
        for j in range(0,cipher_image.shape[1]):
            for k in range(0,3):
                cipher_image[i][j][k] = cipher_image[i][j][k]%256

    cipher_image = cipher_image.astype(np.uint8)
    im = Image.fromarray(cipher_image)
    im.save(folder_path+"/encrypted_image.png")
