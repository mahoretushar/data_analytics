import json

file = open("friends_json.txt", "r")
file_contents = json.load(file)     # reads file and turns into a dictionary
file.close()

print(file_contents['friends'][0])

cars = [
    {"make": "Ford", "model": "Fiesta"},
    {"make": "Ford", "model": "Focus"}
]

file = open("cars_json.txt", "w")
json.dump(cars, file)
file.close()
