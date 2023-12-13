from datetime import date
atual = date.today().year #como pegar o ano atual em que estamos
totmaior = 0
totmenor = 0
for pess in range(0, 7):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade > 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade e {} pessoas menor de idade'.format(totmaior, totmenor))
