# Strings

# Dynamically Typed and Staticaly Typed

course_name_1 = "Python Programming"
course_name_2 = '      Python Programming'

message = """Hi I am Batman 
& I am a Suprehero
& I am friends with Superman"""

# print(course_name_1)
# print(course_name_2)
# print(message)


# function & method

string_length = len(course_name_1)
print(string_length)

# indexing
print(course_name_1[0])
# [start:end]
print(course_name_1[0:4])
print(course_name_1[:4])
print(course_name_1[:])

# -ve indexing
print(course_name_1[-1])
print(course_name_1[-3:-1])

# [start:end:step]
print(course_name_1[::2])

# print a string in reverse order
print(course_name_1[::-1])
