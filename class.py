class student(object):
    count = 0

    def __init__(self,name):
        self.name = name
        student.count += 1


if student.count != 0:
    print('测试失败!')
else:
    bart = student('Bart')
    if student.count != 1:
        print('测试失败!')
    else:
        lisa = student('Bart')
        if student.count != 2:
            print('测试失败!')
        else:
            print('Students:', student.count)
            print('测试通过!')