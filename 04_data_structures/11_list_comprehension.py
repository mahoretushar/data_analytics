products = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 15),
]


# prices = list(map(lambda x: x[1], products))    # list(10, 9, 15) = [10, 9, 15]
prices = [i[1] for i in products]
print(prices)

# filtered_list = list(filter(lambda x: x[1] >= 10, products))
filtered_list = [i for i in products if i[1] >= 10]
print(filtered_list)