#Password generator
import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length = int(input("Enter length: "))
password = ""

for a in range(length):
    password+=random.choice(chars)
    print(password)
