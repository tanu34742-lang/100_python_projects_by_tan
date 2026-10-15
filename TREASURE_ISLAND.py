# THIS IS CODE WHICH WORKS ON IF ,ELSE AND MULTIPLE IF CONDITIONS
# THROUGH THIS CODE YOU WILL GET TO FIND A TREASURE 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print("WELCOME TO THE TREASURE ISLAND")
print("YOUR MISSION IS TO FIND THE TREASURE")

direction = input("you are at a crossroad chosse your direction ? \n left or right :")
if direction == "L":
    swim_wait=input("do you want to swim this lake or you going to wait for the boat ? \nswim or wait : ")
    if swim_wait=="swim":
        print("BUT YOU CAN'T U DUMBASS SO BETTER DIE ")
    if swim_wait=="wait":
        print("NICE CHOICE")
        colour=input("choose a colour ? \n yellow , blue or red : ")
        if colour=="yellow":
            print("GAME OVER")
        elif colour=="red":
            print("GAME OVER")
        else:
            print("YOU WON HURAYYYYY!!")
else:
    print("wrong direction YOU LOST GOODBYEEEEE <3")







    













