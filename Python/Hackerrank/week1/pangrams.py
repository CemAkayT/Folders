#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3


def pangrams(s):

    alp = [chr(l) for l in range(ord('a'), ord('z')+ 1)]
    s = s.lower().replace(' ','')


    for letter in alp:
        if letter not in s:
            return 'not pangram'
    return 'pangram'

test = 'The quick brown fox jumps over the lazy do'

res = pangrams(test)
print(res)