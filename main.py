decryptthis = input("What do you want to decode? (No captitals):  ")
yorndata = input("Do you want to use the word database? (y/n): ")


if yorndata == 'y':
  print ("\n~~!You are using the database!~~\n")

  decrypt = (decryptthis)
  words = ('words.txt')

  for i in range(26):
     word = ''
     for j in range(len(decrypt)):
         extract = ord(decrypt[j])-97
         decrypt_value = ((extract-i) % 26)+97
         word += chr(decrypt_value)
            
     if word in words:
      print("Decrypted word might be:", word)
      print("The Key might be:", i, "\n")
     if word not in words:
      print ("No entries found")
      break

if yorndata == 'n':

  chars = "abcdefghijklmnopqrstuvwxyz"
  rot1 = str.maketrans(chars, chars[1:]+chars[0])


  for i in chars:
    print(decryptthis)
    decryptthis = decryptthis.translate(rot1)



