class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        # self.cars = self.cars.append(car)
        raise NotImplementedError("We can't add cars to the Garage")


ford = Garage()
ford.add_car('Fiesta')
ford.add_car('Fiesta')
print(len(ford))
