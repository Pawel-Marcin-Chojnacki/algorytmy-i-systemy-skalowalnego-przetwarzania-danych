#!/usr/bin/python3
import sys
import os

separator_sign = '\t'
for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split(separator_sign)
	elements = len(words)
	if elements > 1:
		print(words[1],words[0])