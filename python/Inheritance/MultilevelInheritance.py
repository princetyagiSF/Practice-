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

class C(B):#C inherit the B
	def feature5(self):
		print('feature 5 working')

c1=C()
c1.feature1()
c1.feature4()
c1.feature5()
