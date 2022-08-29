# a lambda function is a small anonymous function
# lambda arguments: expression

# def add(a):
#     return a + 10

# x = lambda a: a + 10 


# var_c = add(10)
# print(x(10))

products = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 15),
]


# def sort_item(item):
#     return item[1]


# products.sort(key=sort_item) # 10, 9, 15 = 9, 10, 15
# print(products)


products.sort(key = lambda item: item[1])
print(products)
