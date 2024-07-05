#!/opt/anaconda3/bin/python
 
N = int(input('How many lines? '))
import sys
names = []

for i in range(N):
    print(f'{i+1}.', end=' ')
    line = input().strip()
    names.append(line)

for line in names:
    if len(line) >= 3:
        print(line[2])
    else:
        print('Name is too short')






