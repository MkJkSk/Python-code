Weight = int(input("Enter your Weight:\n"))
command = input("(L)bs   and  (K)g : \n")

if command == "l":
    Kilos = 0.45 * Weight
    print(f"Your  are {Kilos} Kilos")

elif command == "K" or "k":
    lbs = Weight // 0.5
    print(f"Your are the  {lbs} lbs")

else:
    print("Invalid Syntax")
