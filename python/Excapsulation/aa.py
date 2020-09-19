class Car:
	def __init__(self,speed,color):
		self.speed=speed
		self.color=color

	def set_speed(self,value):
		self.speed=value

	def get_speed(self):
		return self.speed

ford=Car(200,'red')
ford.set_speed(200)
ford.speed=400
print(ford.get_speed())
