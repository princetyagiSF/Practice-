#Lambda Expression
#Filter Function

mylist=[1,2,3,4,5,6,7]
#Before Lambda(Check even or odd)
def even(num):
	return num%2==0
def odd(num):
	return num%2!=0
x=filter(even,mylist)
y=filter(odd,mylist)
print(x,y) #Output:-([2, 4, 6, 8], [1, 3, 5, 7])

#Using Lambda in this function
mylist1=[1,2,3,4,5,6,7,8]
evens=filter(lambda num:num%2==0,mylist1)
odd=filter(lambda num:num%2!=0,mylist1)
print(evens,odd) #Output:- ([2, 4, 6, 8], [1, 3, 5, 7]
