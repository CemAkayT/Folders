#!/Users/cemakay/Python/.venv/bin/python


def pagecount(n:int, p:int) -> int:
    from_start = p // 2
    from_end = (n // 2) - (p // 2)
    return min(from_start, from_end)



n = 600
p = 500
res = pagecount(n,p)
print(res)