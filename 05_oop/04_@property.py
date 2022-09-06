class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 42


bruce = WorkingStudent("Bruce Wayne", "Oxford", 200)
print(bruce.name)

bruce.marks.append(90)
bruce.marks.append(75)

print(bruce.average())

clark = WorkingStudent("Clark Kent", "Oxford", 100)
print(clark.school)             # property call
print(bruce.weekly_salary)      # method call - converted to property call
