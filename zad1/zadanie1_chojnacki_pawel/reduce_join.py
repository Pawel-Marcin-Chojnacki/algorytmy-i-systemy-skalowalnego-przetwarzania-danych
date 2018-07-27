#!/usr/bin/python3
import sys

for line in sys.stdin:
    stripped_line = line.strip()
    words = stripped_line.split('\t')
    if words[1] == 'Customers':
        customer = words[0] + '\t' + words[2] + '\t' + words[3] + '\t'
        last_customer_id = words[0]
    elif words[1] == 'Orders':
        if last_customer_id != words[0]:
            continue
        order = words[2] + '\t' + words[3]
        joined_tuple = customer + order
        print(joined_tuple)