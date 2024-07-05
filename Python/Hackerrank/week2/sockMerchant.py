#!/Users/cemakay/Python/.venv/bin/python3

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(ar):
    elem = {x: ar.count(x) for x in ar} # paring and counting
    pairs = {key: value // 2 for key, value in elem.items()} # // integer division/floor division discards the remainder
    
    sum = 0
    for i in pairs.values():
        sum += i # summing the values of the dict
    
    return sum


array = [1, 2, 1, 2, 1, 3, 1, 2, 3, 1, 2, 4, 5, 1, 2, 3, 6]
print(sorted(array))
res = sockMerchant(array)
print(f'We have',res,'pairs')