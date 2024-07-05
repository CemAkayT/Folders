#!/Users/cemakay/Python/.venv/bin/python

with open('tal.txt', 'r') as file:
    sum = 0
    num_lines = 0
    for line in file:
        num_lines += 1
        sum += int(line)
    
print(f'Sum: {sum}')
print(f'Gennemsnit: {sum/num_lines}')







