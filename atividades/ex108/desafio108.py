import moeda

p = float(input('Digite o valor: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)} será {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 13% de {moeda.moeda(p)} será {moeda.moeda(moeda.diminuir(p, 13))}')
