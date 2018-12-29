#创建一个类
class Student():
    #成员属性
    name = 'gao'
    age = 0
    #构造函数

    def __init__(self,name1,age):
        self.name = name1
        self.age = age
        print('Student.name='+Student.name)
    #成员方法
    def print_files(self):
        print('name:'+self.name)
        print('age:'+str(self.age))
    # @classmethod
    # @staticmethod

# def add(x,y):
#     print(x)
#     print(y)

# add(y=20,x=10)

student = Student('johanan gao', 23)
student.print_files()
print(student.name)
