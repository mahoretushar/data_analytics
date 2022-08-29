numbers = [1, 2, 3, 4]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# fourth = numbers[3]

first, second, third, fourth = numbers
print(f"{first}, {second}")

numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 50]

# *args, **args
# first, second, *other = numbers
# print(f"{first}, {second}, {other}")

*other, last_2, last_1 = numbers
print(f"{last_1}, {last_2}")

