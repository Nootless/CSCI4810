from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np
import os

# Adjusted from https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2
def embed(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4    
    
    # how many pixels we can manipulate
    total_pixels = array.size//n

    # delimiter for end of message and length of message
    message += "$n3z0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        raise ValueError("Image size is too small")
    
    index=0
    # goes through total pixels, goes through each pixel's r, g, b
    for p in range(total_pixels):
        for q in range(0, 3):
            if index < req_pixels:
                array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                index += 1

    # reshape and recreate image from newly created arrray
    array=array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save(dest)
    print("Image Encoded Successfully")

def extract(src):
    # open and get pixel info from image

    img = Image.open(src,'r')
    array = np.array(list(img.getdata()))
    n = 0
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    
    total_pixels = array.size//n

    # keeps all the images in groups of 8 bits, ASCII standard rep for characters
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    # used to look through all the 8 bit groupings and find the end of message symbol
    message = ""
    for i in range(len(hidden_bits)):   
        if message[-5:] == "$n3z0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))

    if "$n3z0" in message:
        print("Message:", message[:-5])
    else:
        print("No Hidden Message")

def welcome_message():
    print('Welcome to the secret (shhhh...) Image Board')
    print('Would you like to:\n1.Encode\n2.Decode')
    print('--------------------------------------')
    
if __name__ == '__main__':
    
    welcome_message()
    user_choice = input('Choice: ')

    # hide message
    if user_choice == '1':
        original = input('Enter image path: ')
        message = input('Message to Encrypt: ')
        secret = input('Location to store new Image: ')
        print()
        # original = './images/pingu.png'
        # message = 'hello'
        # secret = './images/pingus.png'

        embed(original,message,secret)
    elif user_choice == '2':
        # 
        secret = input('Enter Secret Image Path: ')
        print()
        extract(secret)
    else:
        print('Invalid Choice')