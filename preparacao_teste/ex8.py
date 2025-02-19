"""
Escreva um programa em Python que pede ao utilizador que lhe forneça
uma sucessão de inteiros correspondentes a valores em segundos e que
calcula o número de dias correspondentes a cada um desses inteiros. O
programa termina quando o utilizador fornece um número negativo. O
seu programa deve possibilitar a seguinte interação:
Escreva um número de segundos
(um número negativo para terminar)
? 45
O número de dias correspondente é 0.0005208333333333333
Escreva um número de segundos
(um número negativo para terminar)
? 6654441
O número de dias correspondente é 77.01899305555555
Escreva um número de segundos
(um número negativo para terminar)
? -1
"""


def dia(valor):
    dias = valor / (24 * 3600)
    return dias


if __name__ == '__main__':
    while True:
        try:
            segundos = int(input('Quantas segundos? '))
            if segundos < 0:
                break
            print(f'{segundos} segundos correspondem a {dia(segundos)} dias.')
        except ValueError:
            print('Digite um valor válido')
    print(f'Adeus!')
