num = [2, 5, 9, 1]
num[2] = 3 #com as listas, é possivel mudar uma variavel dentro da lista, com as tuplas nao é possivel
num.append(7) #vai adicionar o valor 7 ao elemento
num.sort() #coloca todos os itens em ordem
num.sort(reverse=True) #coloca os itens em ordem reversa
num.insert(2, 0) #adiciona mais um numero, sendo possivel escolher a posicao com o index e o numero no object
#num.pop() #elimina o ultimo valor caso vazio, mas colocando numero dentro dos parenteses, retira o que escolher
#num.remove() #vai remover o numero que tu colocar dentro dos parenteses, caso tenha mais de uma vez, vai removar o primeiro apenas
print(num)
print(f'Essa lista tem {len(num)} elementos')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')