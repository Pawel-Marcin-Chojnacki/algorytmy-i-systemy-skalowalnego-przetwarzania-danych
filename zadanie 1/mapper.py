import sys
import re
import os

pattern = """(?:[^a-z0-9]*)([a-z0-9]+[^a-z0-9\n]*[a-z0-9]+)(?:[^a-z0-9]*)"""
#"""(?:[^a-zA-Z0-9]*)([a-zA-Z0-9]+[^a-zA-Z0-9\n]*[a-zA-Z0-9]+)(?:[^a-zA-Z0-9]*)"""
compiled = re.compile(pattern, re.IGNORECASE)

stopwords = set(stopword.strip() for stopword in open('stopwords'))
for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split()
	for word in words:
		m = compiled.match(word)
		if m:
			word = m.group(1)
			word = word.lower()
			if word in stopwords:
				continue
			else:
				print(word + '\t1')