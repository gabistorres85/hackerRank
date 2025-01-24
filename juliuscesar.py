'''Julius Caesar protected his confidential information by encrypting it using a cipher.
 Caesar's cipher shifts each letter by a number of letters. 
 If the shift takes you past the end of the alphabet, 
 just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.'''

# a = 97 z 122
alf ='abcdefghijklmnopqrstuvwxyz'
s = 'middle-Outz'
n= 2
newS=[]
print([ord(char)for char in s])
for char in s:
        if 'a' <= char <= 'z':  # Letras minúsculas
            # Rotação dentro do intervalo de 'a' a 'z'
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            newS.append(new_char)

        elif 'A' <= char <= 'Z':  # Letras maiúsculas
            # Rotação dentro do intervalo de 'A' a 'Z'
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            newS.append(new_char)

        else:  # Caracteres especiais permanecem inalterados
            newS.append(char)


correct = "Dn-/oW/X`SjthvUV"
print([ord(char)for char in newS])
print([ord(char)for char in correct])
print ("".join(newS))
