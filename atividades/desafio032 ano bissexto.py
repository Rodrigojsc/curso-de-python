ano = int(input('Qual ano você quer analisar? '))
if ano % 4 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO.'.format(ano))
