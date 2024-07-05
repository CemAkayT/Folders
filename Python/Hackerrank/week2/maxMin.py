#!/Users/cemakay/Python/.venv/bin/python

import random
def maxMin(k, arr):
    arr = arr[:k]
    print(*arr)
    return max(arr) - min(arr)



# with open('numbers.txt', 'r') as file:
#     numbers = [int(line.strip()) for line in file ]
#     print(numbers)

k = 4
#arr = [10, 4, 1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
arr = [5,2,1,2,1,2,1]

res = maxMin(k, arr)
print(res)