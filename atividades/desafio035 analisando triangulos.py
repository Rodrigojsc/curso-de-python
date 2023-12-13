r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segumento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segumentos de reta podem formar um triângulo.')
else:
    print('Os segmentos de reta não podem formar um triângulo.')
