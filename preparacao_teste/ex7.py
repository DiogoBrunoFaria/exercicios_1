"""
Escreva um programa em Python que lê o número de horas, que um em-
pregado trabalhou numa dada semana e o seu salário/hora e calcula o

ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas fôr menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora, em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
"""

if __name__ == '__main__':
    horas = int(input(f'Quantas horas trabalhou ? '))
    if horas > 40:
        horas_fina = horas * 2
        print(horas_fina)