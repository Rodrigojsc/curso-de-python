pessoas = list()
medidas = list()
cadastro = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    resp = str(input('Deseja continuar? '))
    medidas.append(pessoas[:])
    pessoas.clear()
    cadastro += 1
    if resp in 'Nnãoa':
        print('Certo, listagem concluída')
        break
medidas.sort()
print('-='*30)
for p in medidas:
    if p[1] > 100:
        print(f'{p[0]} tem {p[1]}KG e é pesado')
    else:
        print(f'{p[0]} tem {p[1]} e não é tao pesado.')
print('-=' * 30)
print(f'Lista geral com {cadastro} pessaos cadastradas ')
print(f'{p[:][0]} tem {p[:][1]}KG ')
