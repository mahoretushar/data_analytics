# filter() function return an iterator were the items are filtered through a function

products = [
    ("Product-1", 10),
    ("Product-2", 9),
    ("Product-3", 15),
]


# def filter_function(i):
#     return i >= 10


filtered_list = list(filter(lambda x: x[1] >= 10, products))
print(filtered_list)