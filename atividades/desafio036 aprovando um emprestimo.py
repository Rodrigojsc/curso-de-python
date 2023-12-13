salario = float(input('Qual o seu salário mensal? '))
casa = float(input('Qual será o valor da sua casa? '))
anos = int(input('Em quantos anos deseja terminar de pagar o emprestimo? '))
meses = anos * 12
parcela = casa / meses
pagar = salario * 30 / 100
print('Voce irá demorar {} meses para pagar, com uma parcela mensal de {:.2f}'.format(meses, parcela))
if parcela <= pagar:
    print('Parabéns, você acaba de ter seu crédito de financiamento aprovado!')
else:
    print('Sinto muito, mas não foi possìvel aprovar seu crédito. ')

