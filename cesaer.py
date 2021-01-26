def encryptCesear(txt, s):
	res = ""
	# transverse the plain text
	for i in range(1, len(txt)):
		char = txt[i]
	# Encrypt uppercase characters in plain text
		if (char.isupper()):
			res += chr((ord(char) + s-65) % 26 + 65)
	# Encrypt uppercase characters in plain text
		elif (char.lower()):
			res += chr((ord(char) + s-97) % 26 + 97)
	return res
#check the above function
text = "CEASER CIPHER DEMO"
s = 4
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))

print ("Cipher: " + encryptCesear(text,s))
#plaintext =input("Enter a text: ")
#shift = int(input("enter a shift: "))
#result = encryptCesear (plaintext, shift)
#print(result)
