from time import sleep

num = int(input('Digite o numero que deseja a tabuada: '))
for c in range (0, 11):
    tabuada = num * c
    sleep(.3) # deixar um delay só pra dar um charme kk
    print('{} x {} = {}'.format(num, c, tabuada))
