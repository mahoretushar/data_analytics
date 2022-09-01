from sys import getsizeof

# values get generated at a single instance
values_1 = [x * 2 for x in range(5000000)]
# values only get generated when they are needed
values_2 = (x * 2 for x in range(50000000000000000))

print("List: ", getsizeof(values_1))
print("Tuple: ", getsizeof(values_2))

# for i in values_2:
#     print(i)
