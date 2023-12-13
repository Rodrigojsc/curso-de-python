num = [[], []] #posso fazer assim para conseguir escolher em qual lugar vou colocar o numero na lista menor
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')

"""numeros = list()
separar = list()

for c in range(0, 7):
    numeros.append(int(input('Digite um número: ')))
    separar.append(numeros[:])
    numeros.clear()
    separar.sort()
for p in separar:
    if p[0] % 2 == 0:
        print(f'{p[0]} é par')
    else:
        print(f'{p[0]} é impar')"""
