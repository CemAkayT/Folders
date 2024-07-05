#!/Users/cemakay/Python/.venv/bin/python3


# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

def kangaroo(x1:int, v1:int, x2:int, v2:int) -> str:
    if x1 == x2 and v1 == v2:
        print("YES")

    # Check if kangaroos will never meet (same initial position but different jump distances)
    if x1 == x2 and v1 != v2:
        print("NO")

    # Check if kangaroos have different initial positions and same jump distance
    if x1 != x2 and v1 == v2:
        print("NO")

    # Check if kangaroos have different initial positions and different jump distances
    if v1 != v2 and (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
        print("YES")
    else:
        print("NO")
   
    return ''
    


x1 = 0
v1 = 3
x2 = 4
v2 = 3

res = kangaroo(x1, v1, x2, v2)
print(res)