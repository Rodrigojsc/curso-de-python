"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente:?  '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""
#sem usar mod math

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#usando o mod math