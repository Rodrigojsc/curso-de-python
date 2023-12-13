import math
ang = float(input('Digite o angulo que deseja: '))
math.radians(ang)
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seu seno será {:.2f}'.format(sen))
print('O seu cosseno será {:.2f}'.format(cos))
print('A sua tangente será {:.2f}'.format(tang))
