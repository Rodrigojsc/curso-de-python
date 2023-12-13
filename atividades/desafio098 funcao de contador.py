from time import sleep

def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(.3)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(.3)
        print('FIM')
    print('-=' * 20)


#prog principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
