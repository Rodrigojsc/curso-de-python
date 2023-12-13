#def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')
# precisa deixar duas linhas para o pycharm nao reclamar
#
# programa principal
#soma(b=4, a=3)

def contador(* num):
    print(num)


contador(2, 1, 7)
contador(0, 8)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2  # a lista criada vai passar por aqui para ser dobrada
        pos += 1

valores = [6, 3, 9, 1, 0, 2] # valores que serao dobrados
dobra(valores)
print(valores)
