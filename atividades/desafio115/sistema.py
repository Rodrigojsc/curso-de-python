from desafio115.lib.interface import *
from time import sleep
from desafio115.lib.arquivo import *

arq = 'listadepessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas.', 'Cadastrar novas pessoas.', 'Sair.'])
    if resposta == 1:
        cabecalho('Opção 1')
        # ver pessoas cadastradas no arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
