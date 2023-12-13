peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui a sua altura: '))
altura2 = altura * altura
calculo = peso / altura2
imc = calculo * 10000
print('O seu imc é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
