import random
print ("WELCOME TO THE PASSWORD_GENERATOR !!")
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','e','d','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','^','&','*','(',')']

en_letter=int(input("PLEASE ENTER NUMBER OF LETTERS : "))
en_num=int(input("PLEASE ENTER NUMBER OF NUM  : "))
en_symbol=int(input("PLEASE ENTER NUMBER OF SYMBOLS : "))

pass_l=[]
for char in range(0,en_letter):
    pass_l+=random.choice(letter)
for num in range(0,en_num):
    pass_l+=random.choice(number)
for sym in range(0,en_symbol):
    pass_l+=random.choice(symbol)

#print(pass_l)
random.shuffle(pass_l)
#print(pass_l)

password=""
for char in pass_l:
    password+=char 
print(f"password is {password}")
