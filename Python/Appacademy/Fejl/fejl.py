#!/Users/cemakay/Python/.venv/bin/python

# Exceptions
# https://docs.python.org/3/library/exceptions.html#concrete-exceptions

import sys

fil = input('Hvilken fil skal åbnes?\n')
try:
    file1 = open(fil)
    print(f'\nNu læser jeg indholdet af filen:\n------------------\n{file1.read()}')
except FileNotFoundError as e:
    print(e)

finally:
    print('\n----------------------\nProgrammet er gennemført!')


