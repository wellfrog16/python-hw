#encoding:utf-8

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 80:
            return u'A-优秀'
        if self.__score >= 60:
            return u'B-及格'
        if self.__score <60:
            return u'C-不及格'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
         super(Teacher, self).__init__(name, gender)
         self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course