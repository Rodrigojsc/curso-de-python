idade = int(input('Digite aqui a sua idade: '))
alis = int(input('Você já se alistou? Digite 1 para SIM e 2 para NÃO '))
if alis == 1:
    print('Tudo certo')
elif idade < 17:
    tempo = idade - 17
    print('Ainda tem {} anos antes do sacrificio'.format(tempo))
elif idade == 18 and idade == 17:
    print('Voce deve ir se alistar agora')
elif idade >18:
    print('Voce está atrasado para o alistamento')
else:
    print('Digite apenas numeros')
