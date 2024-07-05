#!//Users/cemakay/Python/.venv/bin/python3


def staircase(height):
    for i in range(1, height+1):
        spaceleft = ' ' * (height - i) # number of spaces = height - i for every iteration
        hashleft = '#' * i           

        print(spaceleft+hashleft)
    return ''
  

res = staircase(5)
print(res)

