import sys

stopwords = set(stopword.strip() for stopword in open('stopwords'))
for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split()
	for word in words:
		word = word.lower()
		if word in stopwords:
			continue
		else:
			print(word)