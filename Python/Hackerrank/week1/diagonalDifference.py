#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def diagonalDifference(arr):
    n = len(arr) # antal rækker

    toright = 0
    toleft = 0

    for i in range(n):
        toright += arr[i][i] # In a square matrix, the row index and column index move together diagonally when iterating over the elements of the diagonal

    for i in range(n):
        toleft += arr[i][n-1-i] #first [i] is row, 

    
    return abs(toright - toleft)

arr = [
    [2,7,22],
    [4,9,12],
    [9,9,24]
]

res = diagonalDifference(arr)

print(res)