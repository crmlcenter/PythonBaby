name = raw_input("What is your name? ")
age = int(raw_input("What is your age? "))
print "Your name is", name, "and your age is", age
from datetime import date
current_year = date.today().year
birth_year = current_year - age
hundred_year = birth_year + 100
print "Hello,",name,"! You will be 100 years old in",hundred_year
if age%2 == 0 and age%3 == 0:
	print "And your curent age is divisible by 2 and 3"
elif age%2 == 0 and age%5 == 0:
	print "And your curent age is divisible by 2 and 5"
elif age%3 == 0 and age%5 == 0:
	print "And your curent age is divisible by 3 and 5"
elif age%2 == 0 and age%7 == 0:
	print "And your curent age is divisible by 2 and 7"	
elif age%3 == 0 and age%7 == 0:
	print "And your curent age is divisible by 3 and 7"		
elif age%5 == 0 and age%7 == 0:
	print "And your curent age is divisible by 5 and 7"	
elif age%2 == 0:
	print "And your current age is divisible by 2"
elif age%3 == 0:
	print "And your current age is divisible by 3"
elif age%5 == 0:
	print "And your current age is divisible by 5"
elif age%7 == 0:
	print "And your current age is divisible by 7"
else:
	print "And your current age is not divisible by 2, 3, 5, or 7. Better luck next year!"

def isEven(num):
	if num%2 == 0:
		print "It is an even number."
	else:
		print "It is an odd number."
isEven(age)