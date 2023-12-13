from random import randint

print('Vamos jogar jokenpo')
jogador = int(input('''Esta são as suas opções, faça uma escolha e boa sorte: 
[0] PEDRA
[1] PAPEL
[2] TESOURA
>>>>>>>>>>>>>>> '''))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada inválida!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
