lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista}')
print(f'Os pares na lista são {pares}')
print(f'Os impares na lista são {impares}')


