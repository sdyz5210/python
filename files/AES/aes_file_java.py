#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# python version 2.7.10

from Crypto.Cipher import AES
import os,sys,random, struct,time

fileInputPath = "/Users/mac/Documents/data/bactive/MiLib114_S3_L001_R1_001.fastq.gz"
fileOutputPath = "/Users/mac/Documents/data/bactive/002.fastq.gz.aes"
fileOutputPath1 = "/Users/mac/Documents/data/bactive/002.fastq.gz"

# ref:https://gist.github.com/crmccreary/5610068
#这是实现了AES的 PKCS#5 / PKCS#7 模式，上面是代码链接
#默认为16
BS = AES.block_size
#pad函数
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#unpad函数
unpad = lambda s : s[0:-ord(s[-1])]

'''
	文件加密
	key:设置的密钥
	chunksize：默认读取的块大小
	使用AES的ECB模式进行加密，AES是块加密算法，每块需要是16的整倍数，如果不能整除需要append一些信息
'''
def aes_ecb_encrypt(key,chunksize=64*1024):
	with open(fileInputPath,'rb') as f1,open(fileOutputPath,'wb') as f2:
		encryptor=AES.new(key,AES.MODE_ECB)
		while True:
			data = f1.read(chunksize)
			if not data:
				break
			elif len(data) % 16 != 0:
				data = pad(data)
			ciphertext=encryptor.encrypt(data)
			f2.write(ciphertext)

'''
	文件解密，文件加密的你操作
	key:设置的密钥
	chunksize：默认读取的块大小
	使用AES的ECB模式进行加密，解密时需要把加密时append上的信息去掉。
'''
def aes_ecb_decrypt(key,chunksize=64*1024):
	filesize = os.path.getsize(fileInputPath)
	count = int(filesize/chunksize) if (filesize%chunksize)==0 else int(filesize/chunksize)+1
	i = 0
	with open(fileOutputPath,'rb') as f1,open(fileOutputPath1,'wb') as f2:
		decryptor=AES.new(key,AES.MODE_ECB)
		while True:
			i = i + 1
			data = f1.read(chunksize)
			if not data:
				break
			if count==i:
				ciphertext=unpad(decryptor.decrypt(data))
			else:
				ciphertext=decryptor.decrypt(data)
			f2.write(ciphertext)

if __name__ == '__main__':
	key = "1234567890abcdef"
	aes_ecb_encrypt(key)
	aes_ecb_decrypt(key)


'''

public static void encryptFile(String sourceFilePath, String destFilePath, String key) {
		File sourceFile = new File(sourceFilePath);
		File destFile = new File(destFilePath);
		if (sourceFile.exists() && sourceFile.isFile()) {
			if (!destFile.getParentFile().exists()) {
				destFile.getParentFile().mkdirs();
			}
			try {
				destFile.createNewFile();
				InputStream in = new FileInputStream(sourceFile);
				OutputStream out = new FileOutputStream(destFile);
				// 转换为AES专用密钥
				SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
				// 创建密码器
				Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
				cipher.init(Cipher.ENCRYPT_MODE, secretKeySpec);
				CipherInputStream cin = new CipherInputStream(in, cipher);
				byte[] cache = new byte[1024];
				int nRead = 0;
				while ((nRead = cin.read(cache)) != -1) {
					out.write(cache, 0, nRead);
					out.flush();
				}
				out.close();
				cin.close();
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			} catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			} catch (NoSuchPaddingException e) {
				e.printStackTrace();
			} catch (InvalidKeyException e) {
				e.printStackTrace();
			}
		}
	}

public static void decryptFile(String sourceFilePath, String destFilePath, String key) {
		File sourceFile = new File(sourceFilePath);
		File destFile = new File(destFilePath);
		if (sourceFile.exists() && sourceFile.isFile()) {
			if (!destFile.getParentFile().exists()) {
				destFile.getParentFile().mkdirs();
			}
			try {
				destFile.createNewFile();
				InputStream in = new FileInputStream(sourceFile);
				OutputStream out = new FileOutputStream(destFile);
				// 转换为AES专用密钥
				SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(), "AES");
				// 创建密码器
				Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
				cipher.init(Cipher.DECRYPT_MODE, secretKeySpec);
				CipherOutputStream cout = new CipherOutputStream(out, cipher);
				byte[] cache = new byte[1024];
				int nRead = 0;
				while ((nRead = in.read(cache)) != -1) {
					cout.write(cache, 0, nRead);
					cout.flush();
				}
				cout.close();
				out.close();
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			} catch (NoSuchAlgorithmException e) {
				e.printStackTrace();
			} catch (NoSuchPaddingException e) {
				e.printStackTrace();
			} catch (InvalidKeyException e) {
				e.printStackTrace();
			}
		}
	}

'''