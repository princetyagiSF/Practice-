#Another technique to use function in python
#check value is int or string before adding
def addnum(num1,num2):
	if type(num1) == type(num2) == type(10):
		print(num1+num2)
	else:
		print('Sorry i need integers')
addnum('2',3) #Output:-Sorry i need integers
