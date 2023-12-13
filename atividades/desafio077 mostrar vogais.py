palavra = ('ler', 'escrever', 'aprender', 'programar', 'estudar', 'criar', 'pensar',
           'falar', 'demonstrar', 'focar', 'trabalhar', 'dificuldade', 'dinheiro',
           'amar', 'indecisao', 'demosntrar', 'avacalhar')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #if ...  in ... '(coloca o grupo de numeros ou letras q deseja achar)':
            print(letra, end=' ')
