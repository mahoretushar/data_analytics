# age should be between 18 and 65
age = 22

# if age >= 18 and age <= 65:
#     print("Eligible")
# else:
#     print("Not Eligible")


# if 18 <= age <= 65:
#     print("Eligible")
# else:
#     print("Not Eligible")


weight = int(input("Enter Weight: "))
command = input("(L)bs and (K)g: ")

if command == "l":
    kilos = 0.45 * weight
    print(f"You are {kilos} kilos")
elif command == "k":
    lbs = weight // 0.45
    print(f"You are {lbs} lbs")
else:
    print("Invalid Option")