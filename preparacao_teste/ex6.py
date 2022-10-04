"""
Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos.
"""

if __name__ == '__main__':
    primeiro = input(f'Insere o primeiro numero')
    segundo = input(f'Insere o primeiro numero')
    terceiro = input(f'Insere o primeiro numero')

    if primeiro == segundo == terceiro:
        print(f'Os numeros são iguais')
    elif primeiro > segundo:
        print(f'O primiero numero é o meior')
    elif primeiro < segundo:
        print(f'O segundo numero é o meior')
    else:
        print(f' o terceiro é o meior')