"""
Escreva um programa em Python que pede ao utilizador que lhe forneça
um inteiro correspondente a um número de segundos e que calcula o nú-
mero de dias correspondentes a esse número de segundos. O seu programa
deve permitir a interação:
"""

if __name__ == '__main__':
    num = int(input(f'Introduza um número em segundos'))
    print(f'Os segundos introduzidos correspondem a {num / 86400} dias')
