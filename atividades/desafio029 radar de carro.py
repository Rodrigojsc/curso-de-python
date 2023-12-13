velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('Multado, excedeu o limite de 80km/h')
    multa = velocidade - 80
    valor = multa * 7
    print('O valor da sua multa é um total de R${:.2f}. Preste atenção ao dirigir'.format(valor))
print('Tenha um bom dia, dirija com segurança')
