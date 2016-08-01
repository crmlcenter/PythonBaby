print "Chapter 3-Week 5"
num = raw_input("Pick a number, any number: ")
num = int(num)
if num == 10:
	print "Good choice"
else:
	print "Bad choice"
print "Done"
num2 = raw_input("Pick another number: ")
num2 = int(num2)
if num2 < 2:
	print "Small number"
elif num2 < 10:
	print "Medium number"
else: 
	print "Large number"
print "Done"
age = raw_input("What is  your age? ")
try:
	age_num = int(age)
	print 'Your age is',age_num 
except:
	print 'Oops, you need to enter a number!'
#Compute 1.5 hourly rate if the employee works over 40 hours
raw_hrs = raw_input("Enter hours: ")
raw_rate = raw_input("Enter rate: ")
hrs = float(raw_hrs)
rate = float(raw_rate)
if hrs <= 40:
	pay = hrs * rate
else: 
	pay = rate * 40 + (rate*1.5 * (hours-40)) 
print "You should get paid", pay
