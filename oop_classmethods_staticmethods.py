class Employee:

  num_of_emps = 0
  raise_amt = 1.04
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.num_of_emps += 1
  
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amount)

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

"""
print(Employee.num_of_emps)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.__dict__)
print(emp_1.__dict__)
emp_1.raise_amount = 1.05
"""

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)
