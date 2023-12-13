numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte,')

while True:
    esc = int(input('Digite um numero entre 0 e 20 para ver seu exemplar por extenso: '))
    if 0 <= esc <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Voce digitou o numero {numeros[esc]}')
