#!/usr/bin/python3
import sys
import os

separator_sign = ' '
previous_value = ''
for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split(separator_sign)
	if previous_value == words[0]:
		print(words[0])
	previous_value = words[0]