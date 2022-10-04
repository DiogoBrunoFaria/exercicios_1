"""
Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
"""

if __name__ == '__main__':
    num = str(input(f'Introduza um numero'))
    nInteiros = ' '
    for x in range(len(num)):
        nInteiros = num[x] + nInteiros
    nNum = num + nInteiros
    print(nNum)