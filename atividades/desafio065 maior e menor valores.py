resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a média foi {}'.format(quant, media))
print('O seu maior numero foi {} e o menor numero digitado {}'.format(maior, menor))
 