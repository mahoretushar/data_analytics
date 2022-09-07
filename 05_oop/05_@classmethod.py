# @classmethod
# @staticmethod

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


bruce = Student("Bruce", "Oxford")

bruce.marks.append(90)
bruce.marks.append(95)

print(bruce.average())

# instance method   - object as first argument
# class method      - class as first argument
# static method     - nothing as first argument


class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)


my_obj = Foo()
my_obj.hi()


class Bar:
    @staticmethod
    def hi():
        print("Hello, I dont take argument.")


another_obj = Bar()
another_obj.hi()
