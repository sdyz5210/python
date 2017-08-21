#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def CreateRSAKeys():
	private_key = RSA.generate(1024)
	public_key = private_key.publickey()

	#保存密钥
	with open("rsakey_priv.pem","w") as f:
		f.write(private_key.exportKey())
	#保存公钥
	with open("rsakey_pub.pem","w") as f:
		f.write(public_key.exportKey())

	return (private_key,public_key)

def testEnAndDe():
	message = "Hello World!!!"
	(private_key,public_key) = CreateRSAKeys()
	cipher = PKCS1_OAEP.new(public_key)
	ciphertext = base64.encodestring(cipher.encrypt(message))
	print ciphertext
	cipher = PKCS1_OAEP.new(private_key)
	msg = cipher.decrypt(base64.decodestring(ciphertext))
	print msg

def encryptByPublicKey():
	message = "Hello World!!!"
	with open("rsakey_pub.pem","r") as f:
		public_key = RSA.importKey(f.read())
	cipher = PKCS1_OAEP.new(public_key)
	ciphertext = base64.encodestring(cipher.encrypt(message))
	print ciphertext
	return ciphertext

def decryptByPrivateKey(ciphertext):
	with open("rsakey_priv.pem","r") as f:
		private_key = RSA.importKey(f.read())
	cipher = PKCS1_OAEP.new(private_key)
	msg = cipher.decrypt(base64.decodestring(ciphertext))
	print msg
#CreateRSAKeys()
ciphertext = encryptByPublicKey()
decryptByPrivateKey(ciphertext)
