import numpy


class SalaryAccount:

    ''' 工资计算类 '''

    def __init__(self, salary):
        self.salary = salary

    def print_salary(self):
        return self.salary


a = SalaryAccount(5000)

# print(s(5000))
# 可以像调用函数一样调用对象的__call__方法

print(a.print_salary())

y = [10, 2, 3]

numpy.multiply(a, 10, out=y)

