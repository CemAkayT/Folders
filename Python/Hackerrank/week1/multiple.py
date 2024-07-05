#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


def fizzBuzz(n):
    for i in range(1, n+1):
        if  i % 3 == 0 and i % 5 == 0:
            print('Multiple of 3 and 5')
        elif i % 3 == 0:
            print('Multiple of 3')
        elif i % 5 == 0:
            print('Multiple of 5')
        else:
            print(i)
        
n = int(input('Enter a number: '))
res = fizzBuzz(n)
print(res)