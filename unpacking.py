numbers = [2,3,4,5,6,7,8,9]

first, second, *other = numbers
print(f"{first} {second} {other}")

*other, Last_2, Last_1 = numbers
print(f"{other} {Last_2} {Last_1} ")

 
 