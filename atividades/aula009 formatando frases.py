frase = 'Curso em video python'
print(frase[0:15])
# [0:...] vai pegar todas as letras escritas

print(frase[2:])
# [2:...] vai pegar da terceira letra em diante, a contagem comeca em 0, 1, 2...

print(frase[0:15:2])
# [...:...:2]vai pegar a frase do comeco ate o 15 e pulando de dois em dois caracteres

print(frase.count('o'))
#vai contar a quantidade de letras 'o' que tem na frase, diferencia letra maiuscula de minuscula

print(len(frase))
#ver o tamanho da frase escrita na variavel

print(len(frase.strip()))
#vai tirar os espaços que tem no comeco e no fim da frase, mas os espaços do meio irão continuar

print(frase.replace('Python', 'Android'))
#vai substituir a palavra python pela android, apenas uma vez, sem alterar a var

#print = frase.replace('Python', 'Android')
#agora sim vai substituir a palavra python por android na var

print('Curso' in frase)
#vai ver se tem curso dentro da frase

print(frase.find('Curso'))
#vai encontrar onde tem Curso escrito

print(frase.split())
#vai separar a frase inteira em palavras, separando espaços e resetando a contagem da frase



print("""Crie um programa que leia o nome completo de uma pessoa e mostra:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome.""")

#c omo printar uma frase com mais de uma linha, usando 3 aspas duplas "
