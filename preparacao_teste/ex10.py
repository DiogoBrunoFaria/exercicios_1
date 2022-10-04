"""
Escreva um programa em Python que lê um número inteiro positivo e
calcula o número obtido do número lido que apenas contém os seus dígitos
impares. Por exemplo,
Escreva um inteiro
? 785554
Resultado: 7555
"""


def par(numero):
    numero = numero % 2
    if numero == 0:
        return
    else:
        return False


if __name__ == '__main__':
    list_num = []
    num = int(input('insira o pirmeiro numero'))
    if par(num):
        list_num.append(num)
        print(list_num)
        num =' '
        for x in range(len(list_num)):
            num += str(list_num[x])

        print(f'Numero so com pares {num}')

