#!/usr/bin/env python3

class Persion(object):
    """
    ���ؾ��и������Ƶ�Person����
    """

    def __init__(self,name):
        self.name=name

    def get_details(self):
        """
        ���ذ����������ַ���
        """
        return slef.name


class Student(Person):
    """
    ����Student ���󣬲���name��branch��year 3������
    """

    def __init__(self,name,branch,year):
        person.__init__(self,name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        ���ذ���ѧ��������Ϣ���ַ���
        """
        return "{} student {} and is in {} year.".format(self.name,self.branch,self.year)

class Teacher(Person):
    """
    ����Teacher���󣬲����ַ����б���Ϊ����
    """
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers
    def get_details(self):
        return "{} teacher {}.".format(self.name,',',join(self.papers))

person = Person('Sachin')
student1 = Student('Kushal','CSE',2005)
teacher1 = Teacher('vich',['C','C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
