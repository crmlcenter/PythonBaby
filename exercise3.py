#Take a list, for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.

#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b_list = []

for element in a_list:
	if element < 5:
		print element

for element in a_list:
	if element < 5:
		b_list.append(element)
print b_list

new_num = int(raw_input ("Enter a number: "))
for element in a_list:
	if element < new_num:
		print element
		
#new_num = raw_input("Enter a number: ")
#try:
#	new_num = int(new_num)
#	for element in a_list:
#		if element < new_num:
#			print element 
#except:
#	print "Oops, you didn't enter a number!"
