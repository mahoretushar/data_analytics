class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Batman', 'Superman']
# print(len(movies))


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage of {self.cars}>'

    def __str__(self):
        return f"This is a Garage for {self.cars}"


ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')
# print(ford.cars)
# print(len(ford))
# print(ford[0])

# for x in ford:
#     print(x)

print(repr(ford))
print(str(ford))
print(type(ford))

number = 10
print(repr(number))
print(str(number))

