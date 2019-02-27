"""
    定义一个学生的类，用来形容学生的

"""
class Student():

    pass

mingyue = Student()

class Python_Student():
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("I do homework")

        return None


yueyeu  = Python_Student()

print(yueyeu.name)
print(yueyeu.age)
# 成员函数没有传入传递参数
yueyeu.doHomework()


