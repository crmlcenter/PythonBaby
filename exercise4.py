#Create a program that asks the user for a number and then prints out a list of all the divisors of that number (a number that divides evenly into another number). 

usernum = int(raw_input("Enter a number larger than 1 to see its divisors: "))
x = range(1,usernum)
for elem in x:
	int(elem)
	if usernum%elem == 0:
		print elem


#Version 1:		
#x = range(1,101)
#usernum = int(raw_input("Enter a number between 1 and 100 to see its divisors: "))
#for elem in x:
#	int(elem)
#	if usernum%elem == 0:
#		print elem
