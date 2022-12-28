import random

letter = int(input("몇 개의 영어? : \n"))
number = int(input("몇 개의 숫자? : \n"))
symbol = int(input("몇 개의 특수 문자? : \n"))


alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbol_list = ["~", "!", "@", "#", "$", "%", "^", "&", "*"]

# password = ""
# for char in range(1, letter + 1):
#     randChar = random.choice(alphabet_list)
#     password += randChar

# for num in range(1, number + 1):
#     randnum = random.choice(number_list)
#     password += randnum

# for sym in range(1, symbol + 1):
#     randsym = random.choice(symbol_list)
#     password += randsym

# print(password)

# difficult version
password_list = []
for char in range(1, letter + 1):
    password_list += random.choice(alphabet_list)

for num in range(1, number + 1):
    password_list += random.choice(number_list)

for sym in range(1, symbol + 1):
    password_list += random.choice(symbol_list)

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for pas in password_list:
    password += pas

print(f"your password is {password}")