largest = None
smallest = None
numlist = []

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
    	num = int(num)
    except:
    	print "Invalid input"
    	continue
    numlist.append(num)

for i in numlist:
	if largest is None:
		largest = i
	elif i > largest:
		largest = i

for g in numlist:
	if smallest is None:
		smallest = g
	elif g < smallest:
		smallest = g

print "Maximum is", largest
print "Minimum is", smallest

#Alternative, much easier way to do it, code goes after line 13
print "Much easier max is", max(numlist)
print "Much easier min is", min(numlist)