message = list(input())
message_a_crypte_en_chiffre = []
message_crypte = 0
for x in range(len(message)):
  message_a_crypte_en_chiffre.append(ord(message[x]))
for l in range(len(message_a_crypte_en_chiffre)-1):
  message_crypte+=message_a_crypte_en_chiffre[l] * message_a_crypte_en_chiffre[l+1]
print(message_crypte)




  
