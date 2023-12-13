#pessoas = {'nome': 'Rodrigo', 'sexo':'M', 'idade':19}  #como é dicionario, tem que declarar com chaves
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #se usar aspas simples dentro dos colchetes, vai dar erro, precisa ser dupla para diferenciar
#print(pessoas.keys()) #vai mostrar as chaves, ex "nome"
#print(pessoas.values()) #vai mostrar os valores, ex "rodrigo"
#print(pessoas.items()) #vai mostrar uma lista composta de 3 tuplas, nesse caso. separando todos
#del pessoas['nome'] #dessa forma, é possivel apagar apenas 1 parametro
#pessoas['nome'] = 'Carlos' #tambem é possivel modificar algum value depois de registrado
#pessoas['peso'] = 67 #posso adicionar outra key e value mesmo depois de registrado. nao preciso dar append
#for k, v in pessoas.items(): #k para keys e v para valores, se inverter a ordem, vai inverter no input tambem
#    print(f'{k} = {v}')

'''brasil = list()
estado1 = {'UF': 'Rio Grande do Sul', 'Sigla': 'RS'}
estado2 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['UF'])'''

estado = dict()
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy()) #maneira alternativa para copiar 
print(brasil)




