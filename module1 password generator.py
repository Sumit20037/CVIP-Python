#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sumit
#
# Created:     18-09-2023
# Copyright:   (c) sumit 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10']
symbols = ['!','@','#','$','+','-','&','(',')','*']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
