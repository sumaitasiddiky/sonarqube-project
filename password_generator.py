#Password Generator Project
import random
import itertools

from more_itertools import random_permutation

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letter = ""
password_symbol = ""
password_number = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
total_length_password= nr_letters + nr_symbols + nr_numbers

print(total_length_password)

for letter in range(1, nr_letters+1):
  random_char = random.choice(letters)
  password_letter = password_letter + random_char
# print(password_letter)

for symbol in range(1, nr_symbols+1):
  random_symbol =random.choice(symbols)
  password_symbol = password_symbol + random_symbol
# print(password_symbol)

for number in range(1, nr_numbers+1):
  random_number =random.choice(numbers)
  password_number= password_number + random_number
# print(password_number)

actual_password = password_letter + password_symbol + password_number

print(actual_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = ''.join(random_permutation(actual_password))

print(hard_password)

# another hard method 
actual_password_list = []

for letter in range(1, nr_letters+1):
  random_char = random.choice(letters)
  actual_password_list += random_char
# print(password_letter)

for symbol in range(1, nr_symbols+1):
  random_symbol =random.choice(symbols)
  actual_password_list += random_symbol
# print(password_symbol)

for number in range(1, nr_numbers+1):
  random_number =random.choice(numbers)
  actual_password_list += random_number

print(actual_password_list)
random.shuffle(actual_password_list)
print(actual_password_list)

difficult_password =""

for char in actual_password_list:
  difficult_password += char

print(difficult_password)



# print(random.shuffle(actual_password_list))

# random_password = ""
# actual_list_1 = [letters, symbols, numbers]

# actual_list = (list(itertools.chain.from_iterable(actual_list_1)))

# for y in range(1, total_length_password+1):
#   hard_pass = random.choice(actual_list)
#   random_password += hard_pass

# print(random_password)






