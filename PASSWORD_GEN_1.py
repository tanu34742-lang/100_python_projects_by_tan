import random
print ("WELCOME TO THE PASSWORD_GENERATOR !!")
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','e','d','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')']

en_letter=int(input("PLEASE ENTER NUMBER OF LETTERS : "))
en_num=int(input("PLEASE ENTER NUMBER OF NUM  : "))
en_symbol=int(input("PLEASE ENTER NUMBER OF SYMBOLS : "))

password=""

#THIS IS THE EASY LEVEL OF PASSWORD USING STRING 
for char in range(0,en_letter):
    password+=random.choice(letter)
for num in range(0,en_num):
    password+=random.choice(number)
for sym in range(0,en_symbol):
    password+=random.choice(symbol)
print(password)

#OUTPUT
WELCOME TO THE PASSWORD_GENERATOR !!
PLEASE ENTER NUMBER OF LETTERS : 5
PLEASE ENTER NUMBER OF NUM  : 4
PLEASE ENTER NUMBER OF SYMBOLS : 3
VvlLy5969@*#
