import datetime

idade = int(input('Em que ano você nasceu? '))
anos =  datetime.date.today().year - idade
if anos <= 9:
    print('A sua categoria é MIRIM')
elif anos <= 14:
    print('A sua categoria é INFANTIL')
elif anos <= 19:
    print('A sua categoria é JUNIOR')
elif anos == 20:
    print('A sua categoria é SENIOR')
else:
    print('A sua categoria é MASTER')
print('Pois você tem {} anos.'.format(anos))
