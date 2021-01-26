while True:
 print("Entrer 1 pour chiffrer ")
 print("Entrer 2  déchiffrer ")
 #print("Other option to exit")
 ch=int(input("votre choix:"))
 if(ch==1):#€ncryption 
  Matrix = [[0 for x in range(5)] for y in range(5)]# matrice 5x5 
  key=input("Entrer la clé:")
  key=list(key) #convertir la clé en une liste
  lstKey= []
  key = [w.replace('i', 'j') for w in key]
  for el in key: # supp les doublons de la liste
   if el not in lstKey:
    lstKey.append(el)
  c2='j'
  j=0
  k=0
  for i in lstKey[:]: # metre le tout en une matrice 5x5
      Matrix[k][j]=i
      j=j+1
      if(j==5):
        j=0
        k=k+1
  if(c2 in lstKey):
   a=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  else:
   a=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for m in lstKey[:]:
    # verifier les elements de la clé et la liste en meme temps 
   #a et les supprimer 
   for n in a[:]:
    if(m==n):
     a.remove(n)
  i=0
  for i in a[:]:
    # inserer les eleemnts de a dans la matrice
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  pt=input("Entrer le message à chiffrer :")

  pt=pt.replace(" ", "")
  pt=list(pt) 
  pt = [w.replace('i', 'j') for w in pt]
  for p in range(0,len(pt)+1):
    #verifier si le message a chiffrer contient
    # des letres adjacents pour qu"on les remplace par X
   if(p+1>=len(pt)):
    break
   elif(pt[p]==pt[p+1]):
    pt.insert(p+1,'x')
  print(pt) 
  sp=[pt[i:i+2] for i in range(0, len(pt), 2)]
  #decouper le message en parties de deux elttre
  cipher=[]
  for i in sp[:]:  
   ls=liste(i) 
   # convertir chaque 2 char du message en une liste
       
   if(len(ls)==1): 
    # si le dernier element est à guache on ajoute x a lui 
    ls.append('x')
   c=0
   w=0
   x=0
   y=0
   z=0
   for t in ls:
    for i in range(0,5):
     for j in range(0,5):
      if(Matrix[i][j]==t):
       if(c==0):
        x = j
        w = i 
        c=c+1
       else:
        z = j 
        y = i    
   if(w==y):
    x = (x + 1) % 5  
    z = (z + 1) % 5 
    cipher.append(Matrix[w][x])
    cipher.append(Matrix[y][z])
   elif(x==z):
    w = (w + 1) % 5 
    y = (y + 1) % 5  
    cipher.append(Matrix[w][x])
    cipher.append(Matrix[y][z])
   else:
    cipher.append(Matrix[w][z])
    cipher.append(Matrix[y][x])
  print("Le text chiffrer est :")
  cipherText = ''.join(cipher)
  print(cipherText)
 elif(ch==2):

  #decryption #meme demarche que le codage 
  Matrix1 = [[0 for x in range(5)] for y in range(5)] 
  lstKey= []
  for el in key:          #effacer les doublons 
   if el not in lstKey:
    lstKey.append(el)
  c2='j'
  j=0
  k=0
  for i in lstKey[:]:   
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  if(c2 in lstKey):
   a=['a','b','c','d','e','f','g','h','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  else:
   a=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for m in lstKey[:]: 
   for n in a[:]:
        # inserer les eleemnts de a dans la matrice

    if(m==n):
     a.remove(n)
  i=0
  for i in a[:]: 
   Matrix[k][j]=i
   j=j+1
   if(j==5):
    j=0
    k=k+1
  pt=cipherText 
  pt=pt.replace(" ", "")
  pt=list(pt) 
  sp=[pt[i:i+2] for i in range(0, len(pt), 2)]
  #decouper le message en parties de deux elttre
  plain=[]
  for i in sp[:]:  
   ls=list(i) 
    # convertir chaque 2 char du message en une liste    
   if(len(ls)==1): 
      # si le dernier element est à guache on ajoute x a lui
    ls.append('x')
   c=0
   w=0
   x=0
   y=0
   z=0
   for t in ls:
    for i in range(0,5):
     for j in range(0,5):
      if(Matrix[i][j]==t):
       if(c==0):
        x = j
        w = i 
        c=c+1
       else:
        z = j 
        y = i    
   if(w==y):
    x = (x - 1) % 5  
    z = (z - 1) % 5 
    plain.append(Matrix[w][x])
    plain.append(Matrix[y][z])
   elif(x==z):
    w = (w - 1) % 5 
    y = (y - 1) % 5  
    plain.append(Matrix[w][x])
    plain.append(Matrix[y][z])
   else:
    plain.append(Matrix[w][z])
    plain.append(Matrix[y][x])
  print("le message en clairr est :")
  plainText = ''.join(plain)
  print(plainText)
 else:
  quit()
