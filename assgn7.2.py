def extract_value(text):
	for letter in text:
		first_digit = -1
		try:
			first_digit = int(letter)
			break
		except:
			continue
	number_start = text.find(str(first_digit))
	number = text[number_start:]
	return float(number)

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
values = []
for line in fh:
	line = line.rstrip()
	if line.startswith("X-DSPAM-Confidence:"):
		values.append(extract_value(line))

result = sum(values) / len(values)
print "Average spam confidence:", result