# OOP in Python - Hướng đối tượng


# Class

class Person:
    __name = ""  # __ = private
    _age = 0  # _ = protected
    male = True  # public

    def __init__(self, name, age, gender):  # Constructor
        self.__name = name
        self._age = age
        self.male = gender

    def get_name(self):
        return self.__name


# Object

obj = Person("KimChi", 15, False)
print(obj.get_name())


# Kế Thừa

class Student(Person):
    __grade = 0

    def __init__(self, name, age, gender, grade):
        super(Student, self).__init__(name, age, gender)
        self.__grade = grade

    def set_grade(self, grd):
        if grd > 0 & grd <= 12:
            self.__grade = grd

    def get_grade(self):
        return self.__grade


# Tao 1 student

std = Student("KimChi", 12, False, 8)
std.set_grade(13)
print(std.get_grade())
print(std.get_name())
