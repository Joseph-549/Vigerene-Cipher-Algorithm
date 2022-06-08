import random


message = "hello"

liste = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X"]
control = 0
keyword = ""

while control < len(message):
    keyword += random.choice(liste).lower()
    control += 1

a = [(ord(i) - 97) + (ord(j) - 97) for i,j in zip(message, keyword)]
b = list(filter(lambda x: x > 26, a))

for filtre in b:
    k = a.index(filtre)
    a[k] = filtre - 26

cipher = ["".join(chr(main + 97).upper() for main in a)]

print("Your Message: ", message)
print("Your Keyword: ", keyword)
print("Your Cipher Message: ", cipher)
































