from random import randint
from time import sleep
from operator import itemgetter  #novo mod para conseguir pegar um numero gerado

jogo = {'jogador 1': randint(1, 20),
        'jogador 2': randint(1, 20),
        'jogador 3': randint(1, 20),
        'jogador 4': randint(1, 20), }
ranking = list()
print('valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado')
    sleep(.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
print('-='*20)
