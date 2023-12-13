num = cont = soma = 0
while True:
    num = int(input('Digite um valor para somar (Ao digitar 999 interrompe): '))
    if num == 999: # ao digitar 999 vai interromper o processo sem calcular o 999
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} numeros e a o resultado foi {soma}.')
#python 3.6+ pode colocar print(f' {} ') que terá mesmo resultado de print(' {} '.format)