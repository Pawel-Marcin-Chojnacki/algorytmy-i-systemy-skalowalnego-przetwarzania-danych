#!/usr/bin/python3
import sys
import os

separator_sign = ' '
previous_value = ''
previous_set = ''
for line in sys.stdin:
	stripped_line = line.strip()
	words = stripped_line.split(separator_sign)
	current_set = words[1]
	value = words[0]
	if previous_value != value and previous_set == 'A':
		print(previous_value)
	previous_value = value
	previous_set = current_set
if previous_value != value and previous_set == 'A':
	print(previous_value)