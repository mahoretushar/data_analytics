class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"    # 12.258963 --> 12.25

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)  # object


number = FixedFloat(12.258963)
new_number = FixedFloat.from_sum(19.2356, 25.3222)
print(new_number)


# Q - What is @staticmethod
# Q - How it works @staticmethod
# Q - Provide real life example @staticmethod


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "ē"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


# money = Euro(80.25647892)
# print(money)
money = Euro.from_sum(16.2534, 62.3256)
print(money)

