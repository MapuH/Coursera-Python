text = "X-DSPAM-Confidence:    0.8475";

for letter in text:
	first_digit = -1
	try:
		first_digit = int(letter)
		break
	except:
		continue

if first_digit == -1:
	print "The string does not contain a number."
	quit()

number_start = text.find(str(first_digit))
number = text[number_start:]

print float(number)