"""
Escreva um programa em Python que lê um número inteiro positivo e
produz o número correspondente a inverter a ordem dos seus dígitos. Por
exemplo,
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
"""

if __name__ == '__main__':
    num = int(input(f'Insrira um numero inteiro'))
    print(num)
    #num = str(num)
    print(f'O Numero invertido é {num[:: -1]}')
