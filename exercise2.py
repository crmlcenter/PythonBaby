#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

user_num = int(raw_input("Enter a number: "))
def isEven(evenodd):
	if evenodd%4 == 0:
		print "This number is a multiple of 4."
	elif evenodd%2 == 0:
		print "This is an even number."
	else:
		print "This is an odd number."
isEven(user_num)

num = int(raw_input("Please enter another number: "))
check = int(raw_input("One more number please: "))
if check%num == 0:
	print "The 2nd number divides evenly into the 1st number- good job."
else:
	print "The 2nd number doesn't divide evenly into the 1st number, try again."