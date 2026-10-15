#uses if-else statments for pizza delivery
print("WELCOME TO THE PIZZA DELVIERY!!")
size=input("enter the size of your pizza : S , M , L ? =")
pepproni=input("do you want pepproni in your pizza : Y or N ? ")
extra_chesse = input("would you like to have extra chesse on it : Y or N ?")
bill=0

if size=="S":
    print("COST OF SMALL PIZZA IS  $15")
    bill=15
    if pepproni=="Y":
        print("pepproni for small pizza would cost extra $2")
        bill+=2
elif size=="M":
    print(" COST OF MEDIUM PIZZA IS $20")
    bill=20
    if pepproni=="Y" or "y":
        print("pepproni for medium pizza would cost extra $3")
        bill+=3
else:
    print("COST OF LARGE PIZZA IS  $25")
    bill=25
    if pepproni=="Y"or "y":
        print("pepproni for large pizza would cost extra $3")
        bill+=3
if extra_chesse=="Y":
    print("AHMMMMMM EXTRA CHESSE WOULD COST YOU SOME CHESSYYY $1 " )
    bill+=1

print(f"YOUR GRAND TOTAL IS ${bill}") 
print("THANKS FOR ORDERING \n VISIT AGAIN !! ")   
