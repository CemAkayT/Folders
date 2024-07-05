#!/Users/cemakay/Python/.venv/bin/python3

# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s:int, t:int, a:int, b:int, apples:list, oranges:list):
    sumapp = 0
    sumoran = 0
    for i in apples:
        if a+i in range(s,t+1):
            sumapp += 1

    for j in oranges:
        if b+j in range(s, t+1):
            sumoran += 1
                
    print(f'{sumapp}\n{sumoran}')   
    return ''  

s = 7
t = 10
a = 4
b = 12
apples = [1,4,-5]
oranges = [3,1, -6]

res = countApplesAndOranges(s,t,a,b,apples, oranges)
print(res)