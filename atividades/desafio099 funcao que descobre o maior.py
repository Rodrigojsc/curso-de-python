from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informandos {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 6, 5, 7, 1)
maior(4, 7, 1)
maior(7, 5)
maior(6)
maior()
