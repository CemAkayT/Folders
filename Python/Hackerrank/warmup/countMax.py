#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def cakeCandles(candles):
    maxh = max(candles)
    print(maxh)
    countmax = candles.count(maxh)
 
    return countmax


arr = [3,2,1,3, 4,2]
res = cakeCandles(arr)
print(res)

