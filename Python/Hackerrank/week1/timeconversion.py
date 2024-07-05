#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

def timeconversion(s):
    if 'AM' in s and s[:2] == '12':
        s = '00' + s[2:8]
        return s
    
    elif 'PM' in s and s[:2] and  s[:2] != '12':
        sstart = int(s[:2]) + 12
        s = str(sstart) +  s[2:8]
        return s
    
    else:
        return s[:8]
    

input = '00:34:56AM'
res = timeconversion(input)
print(res)