Write a program to find the sum of the digits of a number in Python?

A) Python Program to Find Sum of the Digits of a Number

n=int(input("Enter a number:"))
tot=0
while(n>0):
dig=n%10
tot=tot+dig
n=n//10
print("The total sum of digits is:",tot)
Output:

Enter a number:1928
The total sum of digits is: 20
