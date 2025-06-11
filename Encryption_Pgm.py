import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

pt = input("Enter messahe to encrypt: ")
ct = ""
for letter in pt:
    index = chars.index(letter)
    ct += key[index]
    random.shuffle(key)

print(f"Original text: {pt}")
print(f"Encrypted text: {ct}")