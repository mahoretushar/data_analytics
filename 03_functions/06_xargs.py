# *args

def multiply(*numbers):
    total = 1
    for num in numbers:
        total = total * num
    return total
    

# print(total) # scope of variable
print(multiply(1, 2))
print(multiply(1, 2, 5, 6, 7))
print(multiply(1, 2, 4, 5))
