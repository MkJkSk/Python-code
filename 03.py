# print("******** First 10 natural number ***************")
# for i in range(1,11):
#     print(i)
# from calendar import c


def fib(n):
    a = 0
    b = 1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c = a +b
        a = b
        b = c
        print(c) 

fib(int(input("Enter Fib no:")))