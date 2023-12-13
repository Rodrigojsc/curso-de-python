import moeda

p = float(input('Digite o valor: R$ '))
print(f'A metade de R${p:.2f} é R${moeda.metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}')
print(f'Aumentando 10% de R${p:.2f} será R${moeda.aumentar(p, 10):.2f}')
print(f'Diminuindo 13% de R${p:.2f} será R${moeda.diminuir(p, 13):.2f}')
