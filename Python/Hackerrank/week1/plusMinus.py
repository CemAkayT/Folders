#!//Users/cemakay/Python/.venv/bin/python3

def plusMinus(arr):
    n = len(arr)
 
    
    #dict = {item: arr.count(item) for item in arr}
    pos_count = len([+1 for num in arr if num > 0])
    neg_count = len([+1 for num in arr if num < 0])
    zero_count = len([+1 for num in arr if num == 0])

    print("{:.6f}".format(pos_count/n))
    print("{:.6f}".format(neg_count/n))
    print("{:.6f}".format(zero_count/n))




        




arr = [1,1,0,-1,-1]
res = plusMinus(arr)
print(res)