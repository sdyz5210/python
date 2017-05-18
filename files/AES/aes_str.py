#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from Crypto.Cipher import AES
import os,sys,random,struct
from binascii import b2a_hex, a2b_hex

#字符串加密和解密

def encrypt_ecb(key,text , mode=AES.MODE_ECB):
	cryptor = AES.new(key, mode)
	length = 16
 	count = len(text)
	add = length - (count % length)
	text = text + ('\0' * add)
	ciphertext = cryptor.encrypt(text)
	return b2a_hex(ciphertext)

def decrypt_ecb(key,text,mode=AES.MODE_ECB):
	cryptor = AES.new(key, mode)
	plain_text = cryptor.decrypt(a2b_hex(text))
	return plain_text.rstrip('\0')

#AES CBC模式
def encrypt_cbc(key,text , mode=AES.MODE_CBC):
	cryptor = AES.new(key, mode,key)
	length = 16
 	count = len(text)
	add = length - (count % length)
	text = text + ('\0' * add)
	ciphertext = cryptor.encrypt(text)
	return b2a_hex(ciphertext)

def decrypt_cbc(key,text,mode=AES.MODE_CBC):
	cryptor = AES.new(key, mode,key)
	plain_text = cryptor.decrypt(a2b_hex(text))
	return plain_text.rstrip('\0')

if __name__ == '__main__':
	text = "this is a AES example"
	key = '0123456789abcdef'
	text_aes_en = encrypt_ecb(key,text)
	text_aes_de = decrypt_ecb(key,text_aes_en)
	print text
	print text_aes_en
	print text_aes_de
