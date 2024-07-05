#!/Users/cemakay/Python/.venv/bin/python

def zigzag(a, n):

    a.sort()
    mid = int((n + 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]
    print(mid)

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return a


 

ar = [3,5,1,9,6,8,4]
n = len(ar)
res = zigzag(ar, n)
print(res)



# mid = int((n+1)/2)
#     print(mid)
#     n = len(a)
#     a.sort()
#     mid = n // 2
#     return a[:mid] + a[:mid-1:-1]
