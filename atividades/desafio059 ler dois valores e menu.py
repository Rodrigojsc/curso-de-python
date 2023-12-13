from time import sleep
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao =  int(input('Qual é a sua opção? '))
    if opcao == 1:
        resultado = n1 + n2
        print('A soma entre {} e {} será de {}.'.format(n1, n2, resultado))
    elif opcao == 2:
        resultado = n1 * n2
        print('A multiplicação entre {} e {} será de {}.'.format(n1, n2, resultado))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre os dois é {}.'.format(maior))
    elif opcao == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente.')
    sleep(1.5)
print('Fim do programa!')