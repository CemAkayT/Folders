#!/Users/cemakay/Python/.venv/bin/python


# try:
#     tal1 = int(input('Intast første tal: '))
#     tal2 = int(input('Intast andet tal: '))
#     res = tal1/tal2
#     print(f'Resultat: {round(res,2)}')

# except ZeroDivisionError as z:
#     print(f'Fejl: {z}')
   

while True:
    try:
        filnavn = input('Indtast navn på fil: ')
        with open(filnavn):
            print(f'Fil {filnavn} blev fundet.')
            break
    except FileNotFoundError:
        print(f'Fil {filnavn} blev ikke fundet. Prøv igen.')


  
    