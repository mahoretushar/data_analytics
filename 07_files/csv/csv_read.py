file = open("csv_data.txt", "r")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(",")
    name = person_data[0]
    age = person_data[1]
    university = person_data[2]
    degree = person_data[3]

    print(f"{name.title()} is {age}, studying {degree.upper()} at {university.title()}.")


# ["Batman","40","oxford", "computer science"]
sample_csv_value = ",".join(["Batman", "40", "oxford", "computer science"])
print(sample_csv_value)
file = open("csv_write.txt", "w")
file.write(sample_csv_value)
file.close()
