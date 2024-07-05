#!/Users/cemakay/Python/.venv/bin/python


with open('output', 'w') as file:
    for num in range(43,86,2):
        file.write(str(num)+'\n')

    bil = ['Audi', 'Tesla']
    file.write(str(bil))