primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (11 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{} '.format(c))