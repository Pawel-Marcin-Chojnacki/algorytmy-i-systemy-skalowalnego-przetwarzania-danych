import sys

prev_column = 0
summed_output = 0

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    column = int(line[0])
    value = int(line[1])
    if prev_column == column:
        summed_output += value
        continue
    else:
        print(str(prev_column) + '\t' + str(summed_output))
        summed_output = value
        prev_column = column
        continue
print(str(prev_column) + '\t' + str(summed_output))
#print(column)
#     matrix_val = line[1]
#     print('matrix_val: ', matrix_val)
#     vector_val = line[2]
#     print('vector_val', vector_val)
#     if column == prev_column:
#     	summed_output += int(matrix_val) * int(vector_val)
#     	print('summed_output: ', summed_output)
#     else:
#     	summed_output = int(matrix_val) * int(vector_val)
#     	print('summed_output: ', summed_output)
#     print('prev_column: ' + str(prev_column) + 'column: ' + str(column))
#     prev_column = column
# print(summed_output)