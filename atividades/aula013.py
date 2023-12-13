for c in range(0, 6): # (0, 6) o ultimo numero ele sempre ignora, entao sera 0, 1, 2, 3, 4, 5.
    print(c)
print('Fim')

for c in range(6, 0, -1): #  (x, x, -1) o ultimo numero sera a iteração, dessa forma ele faz a contagem regressiva
    print(c)
print('fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('FIm')
