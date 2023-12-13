#estrutura condicional aninhada
nome = str(input('Qual é o seu nome? '))
if nome == 'Rodrigo':
    print('Que nome bonito')
elif nome == 'Junior' or nome == 'Caua' or nome == 'Maria':
    print('SEu nome é bem popular')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}.'.format(nome))
