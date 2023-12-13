expr = str(input('Digite aqui a expressão: '))
pilha = []
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

#o funcionamento se dá ao ler que lenght está em zero, ou seja, caso todos os parenteses abertos se fecharem, está valido, caso contrario dá erro
#pode ser usado para varias coisas que seja necessario verificar duas entradas para validar
