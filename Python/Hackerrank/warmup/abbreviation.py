#!//Users/cemakay/Python/.venv/bin/python3

def abbreviation(a:str, b:str) -> str:
    a = a.upper()
    a = list(a)
    b = list(b)
    notina = [char for char in b if char not in a]
    inb = [char for char in a if char in b]
    print(f'Not in A:', notina)
    print(f'In B:', inb)
    if not notina and inb == b:
        return 'YES'
    else:
        return 'NO'
    
    
   
a = 'daBcd'
b = 'ABCDF' 
res = abbreviation(a,b)
print(res)

