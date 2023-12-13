soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite aqui as idades: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Voce digitou {} numeros pares e a soma dos valores é {}'.format(cont, soma))