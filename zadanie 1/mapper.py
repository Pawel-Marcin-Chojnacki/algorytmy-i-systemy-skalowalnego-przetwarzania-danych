import sys

for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split()
	for word in words:
		print(word + '\t1')