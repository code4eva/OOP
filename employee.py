##########################################################################
# This code is emulated from Mark Lutz's Programming Python
##########################################################################

class Employee(object):
	def __init__(self, name,job=None, salary=0):
		self.name = name
		self.job  = job
		self.salary = salary
	def raised(self, percentage):
		self.salary = (self.salary * (1+percentage))

	def __repr__(self):
		return 'Employee: %s, %s' % (self.name, self.salary)

class Trainer(Employee): 
	def raised(self, percentage, bonus=.05):
		Employee.raised(self, percentage + bonus)


if __name__ == '__main__':
	Richie = Employee('Richard Gere')
	Susan  = Trainer('Susan Polgar', 'trainer', 70000)
	Susan.raised(.20)
	print Susan
