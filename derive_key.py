import sys
import collections
import re
import string
import numpy as np
import cv2
import threading
import sys

cs=string.ascii_lowercase
regular_freq=np.array([8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,0.2,0.8,4.0,2.4,6.7,7.5,1.9,0.1,6.0,6.3,9.1,2.8,1.0,2.4,0.2,2.0,0.1])
regular_freq=(regular_freq/np.amax(regular_freq)*150).astype(int)
key_len=11

def draw_daemon(freq):
	img=np.ones([500,780,3])*255
	n=0
	freq=freq
	fr=freq
	while True:
		n+=1
		n=n%26
		print(n,chr(n+ord('a')))
		fr=np.append(freq[n:],freq[:n])
		img[0:500,0:780]=[255,255,255]
		cv2.imshow("hist",img)
		for i in range(26):
			img[150-regular_freq[i]:150,i*30:(i+1)*30]=[255,0,0]
		for i in range(26):
			img[300-fr[i]:300,i*30:(i+1)*30]=[255,0,0]
		cv2.putText(img,chr(n+ord('a')), (340, 450), cv2.FONT_HERSHEY_PLAIN, 9.0, (0, 0, 255), 2)
		cv2.imshow("hist",img)
		key=cv2.waitKey(0)
		if key==27:   #esc换下一张图
			with open('key.txt','a+') as f:
				f.write(chr(n+ord('a')))
			return
	
if __name__ == "__main__":
	cipher=open('cipher.txt').read()
	cipher="".join(re.findall(r"[a-z]",cipher))
	grouped=[]
	groups=[cipher[i:i+key_len] for i in range(0,len(cipher),key_len)]
	for i in range(0,key_len):
		str1=""
		for group in groups:
			str1+=group[i]
		grouped.append(str1)

	cv2.namedWindow('hist')

	for group in grouped:
		f=collections.Counter(group)
		fr=np.array([f[c] for c in cs])
		draw_daemon((fr/np.amax(fr)*150).astype(int))