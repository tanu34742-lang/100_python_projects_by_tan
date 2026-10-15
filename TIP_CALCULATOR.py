# THIS PROGRAM CALCULATES THE TOTAL TIP GIVEN BY CUSTOMER IN A RESTAURANT


print("WELCOME TO THE TIP CALCULATOR")

bill=float(input("what was the total bill ? =  $"))

tip=int(input("how much tip would you like to give ? 10, 12 or 15 ?  = "))

per=tip/100

num_split = int(input("how many people are going to split the bill? "))

#here use the PERMDASLR THING OR IN SIMPLE LANGUAGE THE PERCEDENCY RULE 
total_tip = ((bill*per+bill)/num_split)

#here i am goin to use round() upto 2 decimal 
print("EACH PERSON WILL PAY = $ ", round(total_tip,2))
