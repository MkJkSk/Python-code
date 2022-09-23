products = [
    ("Products 1", 10),
    ("Products 2",9 ),
    ("Products 3",30 ),
]


prices = [i[1] for i in products]
print(prices)



filtered_list = [i for i in products if i[1]>=10]
print(filtered_list)