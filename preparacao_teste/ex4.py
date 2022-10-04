"""
Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,
"""

if __name__ == '__main__':
    segundos1 = input(f'Por favor, entre com o número de segundos que deseja converter')
    total_segundos = int(segundos1)
    horas1 = total_segundos // 3600
    dias = horas1 // 86400
    segs_restantes = total_segundos % 3600
    minutos = segs_restantes // 60
    segundos_restantes_final = segs_restantes % 60

    if horas1 >= 24:
        dias = int(horas1 / 24)
        horas1 = int(horas1 % 24)

    print(f'{dias} , dias, {horas1}, horas, {minutos}, minutos e {segundos_restantes_final} segundos')