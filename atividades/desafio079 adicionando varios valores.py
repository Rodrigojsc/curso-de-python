valor = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Número repetido, por favor insira um número novo!')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
valor.sort() #para colocar em ordem é necessario adicionar o sort fora do format
print(f'Os valores digitados foram {valor}')
