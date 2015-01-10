"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function."""

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

from_lines = list()
for line in handle:
	line.rstrip('')
	if line.startswith('From '):
		from_lines.append(line)

hours = list()
for line in from_lines:
	hours.append(line[line.find(':')-2:line.find(':')])

hours_count = dict()
for hour in hours:
	hours_count[hour] = hours_count.get(hour, 0) + 1

hours = hours_count.items()
hours.sort()
for hour, count in hours:
	print hour, count