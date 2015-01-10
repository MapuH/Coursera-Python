print "This program will calculate your pay including overtime."

hours = raw_input('Enter hours: ')
try:
	hours = float(hours)
except:
	hours = -1

if hours >= 0:
	print 'You worked', hours, 'hours.'
else:
	print 'Please, enter a valid value.'

rate = raw_input('Enter pay rate: ')
try:
	rate = float(rate)
except:
	rate = -1

if rate >= 0:
	print 'You were paid $%s per hour.' % (rate)
else:
	print 'Please, enter a valid value.'

overtime = hours - 40

if hours > 40:
	pay = (40 * rate) + (overtime * rate * 1.5)
	print 'Your pay is $%s and you worked %s hours overtime.' % (pay, overtime)
else:
	pay = hours * rate
	print 'Your pay is $%s, you did not work overtime.' % (pay)