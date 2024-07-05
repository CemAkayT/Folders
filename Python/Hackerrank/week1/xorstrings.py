#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# XOR = "one or the other then True,if both then False"
# Xoring any bit with O leaves the original binary string unchanged
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'
    return res

if __name__ == '__main__':
    s = input('Type binary:\n')
    t = input()
    print('=========')
    print(strings_xor(s, t))