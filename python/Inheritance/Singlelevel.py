class A:
 	def feature1(self):
 		print('feature 1 working')
	
 	def feature2(self):
 		print('feature 2 working')

class B(A):#B inherit the A
 	def feature3(self):
 		print('feature 3 working')
	
 	def feature4(self):
		print('feature 4 working')

a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
