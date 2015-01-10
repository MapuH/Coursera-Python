score = raw_input('Please, enter a score between 0.0 and 1.0: ')

try:
	score = float(score)
except:
	score = -1

if score > 1:
	print 'Please, enter a valid value.'
elif score >= 0.9:
	print 'A'
elif score >= 0.8:
	print 'B'
elif score >= 0.7:
	print 'C'
elif score >= 0.6:
	print 'D'
elif score >= 0.0:
	print 'F'
else:
	print 'Please, enter a valid value.'