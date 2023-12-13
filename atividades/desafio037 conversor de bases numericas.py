numero = int(input('Digite aqui um numero para ser convertido: '))
print('''Escolha aqui uma das bases para a conversão
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a{}'.format(numero, hex(numero)))
else:
    print('Escolha uma opcão válida.')
