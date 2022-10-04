"""
Dado um conjunto de n inteiros representando notas de alunos, escreva
um programa em Python para determinar quantos tiveram nota positiva.
Modifique o seu programa de modo a também calcular qual a percentagem
de notas positivas.
"""


def notas(nt):
    if nt >= 80 <= 100:
        Nota = 'Muito Bom'
    elif nt >= 60 <= 79:
        Nota = 'Bom'
    elif nt >= 40 <= 59:
        Nota = 'Suf'
    elif nt >= 20 <= 39:
        Nota = 'Infus'
    elif nt >= 0 <= 19:
        Nota = 'Mau'
    return Nota


if __name__ == '__main__':
    nota = int(input('Qual foi a tua nota'))
    print(f'Tens um {notas(nota)}')
