d = float(input('Quantos dias ficou com o carro alugado? '))
km = float(input('Quantos km rodou com o carro durante esse tempo? '))
dias = d * 60
rodou = km * 0.15
total = dias + rodou
print('Voce ficou um total de {:.0f} dias, rodando {:.0f} km, resultando no valor de {:.2f} para o aluguel'.format(d, km, total))
