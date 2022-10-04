"""
Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos
"""
if __name__ == '__main__':
    num = int(input(f'Insere um numero intiero'))
    contador = 0
    zeros = 0
    for zero in num:
        if zero in contador:

