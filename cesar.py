def encrypt(text, s):
    resultat=""
    for i in range(len(text)):
        char = text[i]
        resultat += chr ( ( ord(char) + s - 96) % 26 + 96)
    return resultat
text ="walid"
s = 4
print(encrypt(text,s))