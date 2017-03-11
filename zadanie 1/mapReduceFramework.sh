#!/bin/bash
book=$1
mapper=$2
reducer=$3
result=$4
cat $book | python3 $mapper | sort | python3 $reducer >> $result