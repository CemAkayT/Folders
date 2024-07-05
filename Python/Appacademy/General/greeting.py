#!/Users/cemakay/Python/.venv/bin/python

def bogstav(s:str) -> str:
    return s[::2]

res = bogstav('Hello Houston from America')

print(res)