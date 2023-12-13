cont = soma = 0
while True:
    num = int(input('Digite um valor para somar (Ao digitar 999 interrompe): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} numeros e a o resultado foi {soma}.')
