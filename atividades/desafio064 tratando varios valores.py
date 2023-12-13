#tambem pode ser feito dessa maneira, para economizar linhas: num = cont = soma = 0

num = 0
cont = 0
soma = 0
num = float(input('Digite um numero [999 para parar]: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = float(input('Digite um numero [999 para parar]: '))
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(cont, soma))