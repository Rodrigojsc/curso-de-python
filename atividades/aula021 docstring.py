def teste(b): # a def fica dentro do escopo local, ou seja, ele modifica as var dentro do escopo local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5   # aqui seria o escopo global, ele funciona tanto para fora quanto para dentro,
# mas caso tenha outra var (a) dentro do escopo local, irá valer a var do escopo local para dentro e a var (A) do escopo global para fora.
teste(a)
print(f'A fora vale {a}')

