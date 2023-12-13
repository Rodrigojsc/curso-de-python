pessoa = dict()
escola = []
pessoa['Nome'] = str(input('Nome: '))
pessoa['Nota'] = float(input('Nota: '))
if pessoa['Nota'] > 7:
    pessoa['situção'] = 'aprovado'
elif 5 <= pessoa['Nota'] < 7: #posso colocar o numero antes da variavel ou key, para delimitar um espaco entre 5 e 7
    pessoa['situção'] = 'recuperação'
else:
    pessoa['situção'] = 'reprovado'
for k, v in pessoa.items(): #precisa ser .items para o k e v funcionarem da maneira esperada
    print(f'{k} é igual a {v}')
