def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


a = str(input('Escreva ')).strip()
escreva('palabra muito hrande a a a  ')
escreva(a)


