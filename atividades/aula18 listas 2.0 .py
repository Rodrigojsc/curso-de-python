#teste = list()
#teste.append('Rodrigo')
#teste.append(19)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Maria'
#teste[1] = 22
#galera.append(teste[:])
#print(galera)



#galera = [['Rodrigo', 19], ['Joao', 20], ['Kaua', 21], ['Emilly', 20]]
#print(galera[2][1]) #o primeiro numero dentro dos colchetes, pega a lista entre as 4 existentes, o segundo colchete pega o nome ou a idade.
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')



galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #precisa ter [:] caso contrario nao vai mostrar nada
    dado.clear()

for p in galera:
    if p[1] >= 18: #forma de separar maior de idade para menor de idade de forma facil.
        print(f'{p[0]} é maior de idade') #{p[0]} se refere ao nome da pessoa apos pegar e ver a sua idade dentro da lista maior
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} pessoas maior de idade e {totmen} menor de idade')
