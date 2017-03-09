import sys

pocket = ''
word_counter = 1
key = ''
value = 0
for line in sys.stdin:
	key, value = line.strip().split("\t")
	if key == pocket:
		word_counter = word_counter + int(value)
	else:
		print(key + '\t', word_counter)
		pocket = key
		word_counter = int(value)
if word_counter > 1:
	print(key + '\t', word_counter)
	pocket = key
	word_counter = int(value)