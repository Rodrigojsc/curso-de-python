def calc(a, b):
    s = a * b
    print(f'A área do terreno de {a}x{b} é de {s}m²')


print('Controle de terrenos')
print('-=' * 10)
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
calc(a, b)

