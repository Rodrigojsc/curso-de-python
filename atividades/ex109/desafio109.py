import moeda

p = float(input('Digite o valor: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} será {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)} será {moeda.diminuir(p, 13, True)}')
