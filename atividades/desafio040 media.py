nota1 = float(input('Digite aqui a sua primeira nota: '))
nota2 = float(input('Digite aqui a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua média é {}'.format(media))
if media < 5.0:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
