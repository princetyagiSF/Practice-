class A:
	def feature1(self):
		print('feature 1 working')
	
	def feature2(self):
		print('feature 2 working')
class B:
	def feature3(self):
		print('feature 3 working')
	
	def feature2(self):
			print('feature 4 working')

class C(A,B):
	def feature5(self):
		print('feature 5 working')
		
c1=C()
c1.feature1()
c1.feature3()
c1.feature5()
