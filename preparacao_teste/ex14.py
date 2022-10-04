"""
Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
"""


def digito(valor):
    valor = str(valor)
    digitos = 0
    for x in range(len(valor)):
        digitos += int(valor[x])

    return digitos


if __name__ == '__main__':
    num = int(input('Qual é o número? '))

    print(f'O número {num} contém {digito(num)} em soma de seus digitos.')
