#!/Users/cemakay/DataScience/Jupyter/.venv/bin/python

def birtdays(s: list, d: int, m: int) -> int:
    count = 0

    if m > len(s):
        print('Month sequence gt than the length of the list')

    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            count += 1
    return count

s = [1,2,1,3,2,5,2]
d = 4
m = 3
res  = birtdays(s,d,m)

print(res)





