from random import randint
v = 0
print('-'*30)
while True:
    jogador = int(input('Diga um numero entre 0 e 10: '))
    comp = randint(0, 11)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}. total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 40)
    print('Vamos jogar novamente?')
print('-+-'*16)
print(f'GAME OVER!!! Você venceu {v} vezes antes de perder.')
print('-+-'*16)
