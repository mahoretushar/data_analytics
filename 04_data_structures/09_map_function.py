# map() function executes a specified function for each item in an iterable
# map(function, iterable)

products = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 15),
]


# prices = []
# for x in products:
#     prices.append(x[1])

prices = list(map(lambda x: x[1], products))    # list(10, 9, 15) = [10, 9, 15]
# x = ("Product-1", 10):    return x[1] = 10
# x = ("Product-2", 9) :    return x[1] = 9
# x = ("Product-3", 15):    return x[1] = 15
print(prices)