def multiply(*numbers):
    total  = 1
    for num in numbers:
        total = total * num
    return total



print(multiply(2,2))
print(multiply(1,2,5,6,7,8,9))
print(multiply(1,2,4,5,7,8))