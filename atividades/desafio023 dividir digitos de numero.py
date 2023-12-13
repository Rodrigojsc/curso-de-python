numeros = int(input('Digite um numero '))
u = numeros // 1 % 10
d = numeros // 10 % 10
c = numeros // 100 % 10
m = numeros //1000 % 10
print('Analisando numero{}'.format(numeros))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
