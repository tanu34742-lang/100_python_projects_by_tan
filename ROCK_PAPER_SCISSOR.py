import random


print("WELCOME TO THE ROCK PAPER AND SCISSORS GAME")
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''')

paper=('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')


scissor=('''


    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')
game_image=[rock,paper,scissor]
your_choice=int(input("What do you want to chose ? Type 0 for Rock , 1 for Paper or 2 for Scissor : \n "))
print(game_image[your_choice])

computer_chose=random.randint(0,2)
print(f"computer choose :{computer_chose}")
print(game_image [computer_chose])

if your_choice>=3 or your_choice<0:
    print("the number is invalid you loose")
elif your_choice==0 and computer_chose==2:
    print("you win")
elif your_choice==2 and computer_chose==0:
    print("you loose")
elif computer_chose>your_choice:
    print("you loose")
elif computer_chose<your_choice:
    print("you win")
elif computer_chose==your_choice:
   print("DRAW")    




