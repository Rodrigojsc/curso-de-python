valor = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o ultimo valor: ')))
print(f'Voce digitou os valores {valor}')
print(f'O valor 9 apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O valor 3 apareceu na {valor.index(3)+1}ª posição ')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')
