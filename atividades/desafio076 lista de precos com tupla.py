tup = ('Pão', 0.25,
       'Coxinha', 3,
       'Pastel', 6,
       'Sonho', 2.5,
       'Brigadeiro', 1.25,
       'Rocambole', 7)
print('-=-'*12)
print(f'{"LISTAGEM DE PREÇOS":^40}') #consigo centralizar usando format e :^40 ou qlqr numero
print('-=-'*12)
for pos in range(0, len(tup)):
    if pos % 2 == 0: #usei para conseguir separar as posicoes pares das impares, conseguindo arrumar onde fica cada coisa
        print(f'{tup[pos]:.<30}', end='')
    else:
        print(f'R${tup[pos]:>5.2f}')
print('-=-'*12)
