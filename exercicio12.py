la = int(input('Digite o lado A: '))
lb = int(input('Digite o lado B: '))
lc = int(input('Digite o lado C: '))

if la == lb == lc:
    print('Equilátero!')
elif la == lb or lb == lc or lc == la:
    print('Isóceles!')
elif la != lb != lc:
    print('Escaleno!')