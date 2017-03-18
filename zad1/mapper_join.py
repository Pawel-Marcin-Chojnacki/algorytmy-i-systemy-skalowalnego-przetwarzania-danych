#!/usr/bin/python3
import sys

for line in sys.stdin:
    stripped_line = line.strip()
    words = stripped_line.split('\t')
    if words[0] == 'Orders':
        key = words[2]
        value = words[0] + '\t' + words[1] + '\t' + words[3]
        print(key + '\t' + value)
    if words[0] == 'Customers':
        key = words[1]
        value = words[0] + '\t' + words[2] + '\t' + words[3]
        print(key + '\t' + value)