viagem = int(input('Qual será a distância da sua viagem? '))
valor1 = viagem * 0.5
valor2 = viagem * 0.45
if viagem < 201:
    print('O valor da sua viagem será de R${:.2f}'.format(valor1))
else:
    print('O valor da sua viagem será R${:.2f}. Você está participando de uma promoção.'.format(valor2))

#maneira que o professor fez
distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua viagem será de R${:.2f}'.format(preco))
