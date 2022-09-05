# classes are the blueprints of objects
# class = Human Being - eyes, ears.....
# object = 'Bruce Wayne' - eyes, ears....

my_student = {
    'name': 'Bruce Wayne',
    'grades': [70, 80, 85, 90],
    # 'average_grades': cal,
}


def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


# print(average_grade(my_student))


class Student:
    def __init__(self, new_name, new_grades):   # constructor
        self.name = new_name
        self.grades = new_grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('Bruce Wayen', [70, 80, 85, 90])
student_two = Student('Clark Kent', [60, 60, 45, 50])

print(student_one.name)
print(student_two.name)

print(student_one.average_grade())
