numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi digitado.')

