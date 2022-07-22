from Crypto.Cipher import DES
from secrets import token_bytes
from PIL import Image
import matplotlib.pyplot as plt

#Taken three key from token bytes

key1=token_bytes(16)
key2=token_bytes(16)
key3=token_bytes(16)

#Encryption function using triple key

def encrypt(image):
  cipher1=DES.new(key1[0:8],DES.MODE_CBC,key1[8:16])
  ciphertext1=cipher1.encrypt(image)
  cipher2=DES.new(key2[0:8],DES.MODE_CBC,key2[8:16])
  ciphertext2=cipher2.decrypt(ciphertext1)
  cipher3=DES.new(key3[0:8],DES.MODE_CBC,key3[8:16])
  ciphertext3=cipher3.encrypt(ciphertext2)
  return ciphertext3

#Taken the image path from the user

path=input("enter the path of the image")

# open image and show the image

img= Image.open(path)
plt.imshow(img)

# Main function for process the image and call the encryption function
with open(path, 'rb') as imagefile:
  image=imagefile.read()
while len(image)%8!=0:
  image+=b" "
ciphertext=encrypt(image)
print(image)
#print the encrypted from of the image
print(ciphertext)

# Decryption function
# Encryption and Descryption key is same

def decrypt(ciphertext):
  cipher1=DES.new(key3[0:8],DES.MODE_CBC,key3[8:16])
  plaintext1=cipher1.decrypt(ciphertext)
  cipher2=DES.new(key2[0:8],DES.MODE_CBC,key2[8:16])
  plaintext2=cipher2.encrypt(plaintext1)
  cipher3=DES.new(key1[0:8],DES.MODE_CBC,key1[8:16])
  plaintext3=cipher3.decrypt(plaintext2)
  return plaintext3

# call the decryption function

plaintext=decrypt(ciphertext)

# Converting data to image
# In epath we can use any path where we want to save data
# After that that the data will be converted into image

epath="/content/untitled"
with open(epath, 'wb') as image_file:
	image_file.write(plaintext)
img=Image.open("/content/untitled")
plt.imshow(img)