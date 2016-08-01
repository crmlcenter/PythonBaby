print "Week 6- Chapter 4"
def hello():
	print "Hello"
	print "Fun"

hello()
print "Hi"
hello()

big = max("Hello world")
print big
tiny = min("1234")
print tiny

def computepay(h,r):
	if h > 40:
		pay = r*40 + (r*1.5 * (h-40)) 
	else:
		pay = r*h
	return pay

hrs = raw_input("Enter hours: ")
rate = raw_input("Enter rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h,r)
print p