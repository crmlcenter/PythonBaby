shoppinglist = []

add_item = raw_input("What would you like to add? ")
shoppinglist.append(add_item)
for element in shoppinglist:
	print "You need to buy:",(element)