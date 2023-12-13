valor = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))

    if c == 0 or n > valor[len(valor)-1]:
        valor.append(n)
    else:
        pos = 0
        while pos < len(valor):
            if n <= valor[pos]:
                valor.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores da lista em ordém será {valor}')


