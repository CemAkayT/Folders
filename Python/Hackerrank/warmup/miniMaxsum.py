#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:-1])
    max = sum(arr[-1:0:-1])
    print(min,max)
    return ''


arr = [1,3,5,7,9]
res = miniMaxSum(arr)
print(res)

