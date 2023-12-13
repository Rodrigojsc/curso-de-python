sal = int(input('Digite aqui qual o seu salario atual para receber seu aumento: '))
if sal <= 1250:
    aumento = sal / 100 * 115
    print('O seu novo salário será R${}'.format(aumento))
else:
    aumento = sal / 100 * 110
    print('O seu novo salário será de R${}.'.format(aumento))
