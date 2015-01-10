fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()
for line in fh:
    line = line.rstrip()
    lines = line.split()
    words = words + lines

for word in words:
	if word not in lst:
		lst.append(word)
	else:
		continue

lst.sort()
print lst