  
char_str = 'walid'
  
# printing original string 
print("Le mot original : " + char_str) 
  
# decalage a guache et a droite   
r_rot = 4 
l_rot = 3
  
# deca gauchet droite

# Utilisation de mod et decoupage de la chainede charactere
temp = (r_rot - l_rot) % len(char_str) 
res = char_str[temp : ] + char_str[ : temp] 
  
# affiche le resultat 
print("la chaine apres rotation  : " + str(res))  