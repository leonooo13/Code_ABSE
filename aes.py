import hashlib

from Crypto.Cipher import AES
key=b'123456'
text=b'messge'
iv=b'123423'
# aes=AES.new(key,AES.MODE_CBC,iv)
# cc=aes.encrypt(text)
# print_tb(cc)
md5=hashlib.md5(key)
print(md5)
