clubes = [ 'Flamengo',
           'Vasco',
           'Botafogo',
           'Palmeiras',
           'Gremio'
           ]
clube = input('Digite o clube desejado: ')
find = False
for i in range(len(clubes)):
    if clube.upper() == clubes[i].upper():
        find= True
if find:
    print('Achei o time!')
else:
    print('Não achei o time.')