def reversText(m):
	trslt = ''
	i = len(m)-1
	while i >= 0:
		trslt = trslt + m[i]
		i -= 1
	print("reverse is :", trslt)

Text = input("Enter a text: ")
reversText(Text)

##message = 'This is program to explain reverse cipher.'
#translated = '' #cipher text is stored in this variable
#i = len(message) - 1

#while i >= 0:
 #  translated = translated + message[i]
 #  i = i - 1
#print("The cipher text is : ", translated)

