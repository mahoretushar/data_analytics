letters = ['a', 'd', 'b', 'c', 'd', 'e', 1, 2, 3, 'd']

# find index of 'b'
print(letters.index(2))

# print(letters.index('z'))   # generates an error


# in keyword is used for checking the existence
if 'z' in letters:
    print(letters.index('z'))
else:
    print("Letter not Found")

# to check total number of occurences
print(f"Number of d's in list: {letters.count('d')}")
