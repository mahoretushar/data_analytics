letters = ['a', 'b', 'c', 'd', 'e', 'gg']

# adding
letters.append('z')
letters.insert(0, 'x')
# print(letters)

# removing
# letters.pop()   # pops the last element from the list
# letters.pop(2)  # pops the element at specified index
letters.remove('gg')

print(letters)

# another way to remove an item is by using del
del letters[0]
# we can delete the range of items in the list
del letters[:3]
print(letters)

# to delete entire list
letters.clear()
print(letters)
