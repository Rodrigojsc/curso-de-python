from time import sleep

while True:
    num = int(input('Digite o numero que deseja a tabuada: '))
    if num < 0:
        break
    print('--' * 10)
    for c in range (1, 11):
        tabuada = num * c
        sleep(.3) # deixar um delay só pra dar um charme kk
        print('{} x {} = {}'.format(num, c, tabuada))
    print('--' * 10)
print('Tabuada encerrada')
