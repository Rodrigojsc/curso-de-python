def notas(*n, sit=False):
    """
    -> funcao para analisar varias notas
    :param n: uma ou mais notas dos alunos, aceita varias
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacoo
    :return:dicionario com varias informacoes sobre a situacao da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'MEDIA'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 1.5, 3, 8.5, sit=True)
print(resp)
help(notas)





