l1 = [10,20,30,40,50,60,70,80,90]
print(l1,type(l1))
n= int(input("Enter Your number: \n"))
if n in l1:
    print(l1.index(n))
else:
    print(f"\tValue {n} is not present in the List,try again\t")