"""
Escreva um programa em Python que pede ao utilizador que lhe forneça
um número e que escreve a tabuada da multiplicação para esse número.
O seu programa deve gerar uma interacção como a seguinte:
"""

if __name__ == '__main__':
    while True:
        try:
            num = int(input(f'Insere um numero inteiro para fazer uma taboada'))
            for x in range(1, 11):
                mult = x * num
                print(f'{num} * {x} = {mult}')
                x += 1
            break

        except ValueError:
            print('Digite um valor válido')


