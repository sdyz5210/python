#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from Crypto.Cipher import AES
import os,sys,random, struct

fileInputPath = "/Users/mac/Documents/data/rocky/test1.fastq.gz"
fileOutputPath = fileInputPath + ".enc"
fileOutputPath1 = "/Users/mac/Documents/data/rocky/test2.fastq.gz"

def aes_cbc_encrypt(key,chunksize=64*1024):
	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	encryptor = AES.new(key, AES.MODE_CBC, iv)
	filesize = os.path.getsize(fileInputPath)
	with open(fileInputPath,'rb') as f1,open(fileOutputPath,'wb') as f2:
		f2.write(struct.pack('<Q', filesize))
		f2.write(iv)
		while True:
			data = f1.read(chunksize)
			if not data:
				break
			elif len(data) % 16 != 0:
				data += ' ' * (16 - len(data) % 16)
			f2.write(encryptor.encrypt(data))

def aes_cbc_decrypt(key,chunksize=64*1024):
	with open(fileOutputPath,'rb') as f1,open(fileOutputPath1,'wb') as f2:
		origsize = struct.unpack('<Q', f1.read(struct.calcsize('Q')))[0]
		iv = f1.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		while True:
			data = f1.read(chunksize)
			if not data:
				break
			ciphertext=decryptor.decrypt(data)
			f2.write(ciphertext)
		f2.truncate(origsize)

def aes_ecb_encrypt(key,chunksize=64*1024):
	filesize = os.path.getsize(fileInputPath)
	iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
	with open(fileInputPath,'rb') as f1,open(fileOutputPath,'wb') as f2:
		encryptor=AES.new(key,AES.MODE_ECB)
		f2.write(struct.pack('<Q', filesize))
		f2.write(iv)
		while True:
			data = f1.read(chunksize)
			if not data:
				break
			elif len(data) % 16 != 0:
				data += ' ' * (16 - len(data) % 16)
			ciphertext=encryptor.encrypt(data)
			f2.write(ciphertext)

def aes_ecb_decrypt(key,chunksize=64*1024):
	with open(fileOutputPath,'rb') as f1,open(fileOutputPath1,'wb') as f2:
		decryptor=AES.new(key,AES.MODE_ECB)
		origsize = struct.unpack('<Q', f1.read(struct.calcsize('Q')))[0]
		iv = f1.read(16)
		while True:
			data = f1.read(chunksize)
			if not data:
				break
			ciphertext=decryptor.decrypt(data)
			f2.write(ciphertext)
		f2.truncate(origsize)

if __name__ == '__main__':
	key = "1234567890abcdef"
	aes_cbc_encrypt(key)
	aes_cbc_decrypt(key)
	#aes_ecb_encrypt(key)
	#aes_ecb_decrypt(key)