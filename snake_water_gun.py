# this game uses random module and list for completing the game 

import random 
print("WELCOME TO THE GAME OF SNAKE WATER AND GUN")

snake=('''
 --..,_                     _,.......
       `'.'.                .'`__ o  `;__.      
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
              ''')


water=('''
       ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
    ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
 ~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~^~
''')

gun=('''
 ,--^----------,--------,-----,-------^--,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,-------, _________________________|
     / XXXXXX /`|     /
    / XXXXXX /  `\   /
   / XXXXXX /\______(
  / XXXXXX /
 / XXXXXX /
(________(
 `------'
 ''')


game_image=[snake,water,gun]

user_choice= int(input("enter a number of your choice 0 for snake  , 1 for water and 2 for gun : "))
print(game_image[user_choice])

computer_choice=random.randint(0,2)
print(f"computer chooses : {computer_choice}")
print(game_image[computer_choice])

if user_choice>=3 or user_choice<0:
    print("sorry invalid number you loose !! \n  booooh !!")
elif user_choice==0 and computer_choice==2:
    print("COMPUTER WON !! ")
elif user_choice==2 and computer_choice==0:
    print("YOU WON !!")
elif user_choice<computer_choice:
    print("YOU WON")
elif user_choice>computer_choice:
    print("COMPUTER WON")
elif user_choice==computer_choice:
    print("DRAW")
print("HOPE YOU ENJOYED THE GAME !! ")
