# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Initialized SchoolMember:{}'.format(self.name))

    def tell(self):
        print("name is {} and age is {}".format(self.name, self.age))


class Person:
    def __init__(self, sex):
        self.sex = sex
        print('Initialized Sex is {}'.format(self.sex))

    def tell(self):
        print('sex is {}'.format(self.sex))


class Teacher(Person, SchoolMember):
    def __init__(self, name, age, salary, sex):
        SchoolMember.__init__(self, name, age)
        Person.__init__(self, sex)
        self.salary = salary
        print('Initailized Teacher:{}'.format(self.name))
    #
    # def tell(self):
    #     SchoolMember.tell(self)
    #     print('Salary is {}'.format(self.salary))


teacher = Teacher("Jcb", 11, 20000, 'M')
teacher.tell()

