valores = []
mai = men = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('-=-'*20)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end=' ')
print(f'\nO menor valor foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print('')
