media = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher18 = 0
for p in range(1, 5):
    print('-----{}ª pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    media += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 18:
        totmulher18 += 1
mediaidade = media / 4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulheres menores de idade'.format(totmulher18))
