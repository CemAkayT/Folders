#!/Users/cemakay/Python/.venv/bin/python

class HTMLFormatError(Exception):
    pass


test = input('Indtast første linje ')

if(test != '<html>'):
    raise HTMLFormatError

print('OK')