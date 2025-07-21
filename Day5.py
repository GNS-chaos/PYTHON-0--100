#loops
#for item in listofitems

fruits=["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")

student_scores=[15,9,35,65,95,2,5,49,35,9,98,51,68,31,54,8]
total=sum(student_scores)
print(total)

sum=0

for score in student_scores:
    sum+=score
print(sum)

print(max(student_scores))

max_score=0
for score in student_scores:
    if score>max_score:
        max_score=score


#range function
#for number in range(a,b):

for number in range(1,10,3): #10 is not included #3is the aralık
    print(number)

gauss=0
for number in range(1,101):
    gauss+=number
print(gauss)

#pypassword generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
for char in range(0,nr_letters):
    password+=random.choice(letters)
for char in range(nr_numbers):
    password+=random.choice(numbers)
for char in range(0,nr_symbols):
    password+=random.choice(symbols)
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
    password+=char
print(password)

