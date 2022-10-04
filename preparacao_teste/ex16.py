"""
Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
Escreva um número
-> 347
347743
"""

if __name__ == '__main__':
    valor = int(input(f'Insira um numeros'))
    num = str(valor)
    print(f'{valor}{num[:: -1]}')
