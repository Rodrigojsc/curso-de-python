valor = int(input('Digite aqui o valor da sua compra: '))
metodo = float(input('''Escolha o seu método de pagamento
[1] a vista com 10% de desconto
[2] a vista no cartão com 5% de desconto
[3] em até 2x no cartão
[4] 3x ou mais no cartão com acréscimo de 20%
Digite aqui: '''))
porcentagem = valor / 100
preco1 = porcentagem * 90
preco2 = porcentagem * 95
preco4 = porcentagem * 120
if metodo == 1:
    print('Você irá pagar R${:.2f}.'.format(preco1))
elif metodo == 2:
    print('Você irá pagar R${:.2f}.'.format(preco2))
elif metodo == 3:
    print('Você irá pagar R${:.2f} em 2x de {:.2f}'.format(valor, valor / 2))
elif metodo == 4:
    parc = int(input('Em quantas vezes será? '))
    parcela = preco4 / parc
    print('Você irá pagar R${:.2f} parcelas de R${:.2f}'.format(preco4, parcela))
else:
    print('Digite um numero válido.')
