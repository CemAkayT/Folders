#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


def timeconversion(s):
    if s[-2:] == 'PM':
        start = int(s[:2]) + 12
        start = str(start)
        rest = s[2:-2]
        return start+rest
        
    elif s[-2:] == 'AM' and int(s[:2]) >= 12:
        st = int(s[:2]) -12
        st = str(st)
        rest = str(0)+s[2:-2]
        return st+rest
    
    return 'a'

s = '04:59:59AM'
res = timeconversion(s)
print(res)