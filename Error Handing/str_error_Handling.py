l1 = ['P','Y','T','H','O','N']
print(l1,type(l1))
m = input("Enter Your string: \n")
if m in l1:
    print(l1.index(m))
else:
    print(f"\tValue {m} is not present in the List,try again\t")    