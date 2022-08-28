from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-='*9)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-='*9)
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*14)
print('O Jogador jogou : {}'.format(itens[jogador]))
print('O computador jogou: {}'.format(itens[computador]))
print('-='*14)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('Jogador VENCEU!!')
    elif jogador == 2:
        print('Computador VENCEU!!')
    else:
        print('Jogada inválida')
elif computador == 1: #Computdor jogou PAPEL
    if jogador == 0:
        print('Jogador Venceu!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('Jogador Venceu!!')
    else:
        print('Jogada inválida')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('Jogador Venceu!!')
    elif jogador == 1:
        print('Computador Venceu!!')
    elif jogador == 2:
        print('EMPATE!!')
    else:
        print('Jogada inválida')