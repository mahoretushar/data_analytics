class Student:
    def __init__(self, name):
        self.name = name


movies = ['Matrix', 'Batman', 'Superman']
print(len(movies))


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('focus')
print(ford.cars)
print(len(ford))
print(ford[0])

for x in ford:
    print(x)
