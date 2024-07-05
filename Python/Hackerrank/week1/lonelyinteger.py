#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
import random
def lonelyinteger(intlist):
    lonely= [num for num in intlist if intlist.count(num) == 1]
    return sum(lonely) if lonely else None
    
    


rand = [1,2,3,4,5,4,3,2,1]
print(rand)

res = lonelyinteger(rand)
print(res)