# sets are the collection with no duplicates

numbers = [1, 1, 2, 3, 4, 5, 5, 5]
uniques = set(numbers)
print(uniques)
books_collections = {"b1", "b2", "b3", "b4"}


first_set = set(numbers)
second_set = {7, 8}

second_set.add(10)      # {7, 8, 10}
second_set.remove(7)    # {8, 10}

# print(second_set[1])    # we cannot use indexing with set


print(first_set | second_set)   # union
print(first_set & second_set)   # intersection
print(first_set - second_set)   # difference
print(first_set ^ second_set)   # symetric diff

# {1, 2, 3}  {3, 4, 5}
# union = {1, 2, 3, 4, 5}
# intersection = {3}
# diff = {1, 2}
# s diff = {1, 2, 4, 5}
