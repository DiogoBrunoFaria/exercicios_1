"""
    primeiro ex
    """
if __name__ == '__main__':
    x = int(input(f'Escreva o primeiro numero '))
    y = int(input(f'Escreva o segundo numero '))
    z = (x + 3 * y) * (x - y)
    print(f'O valor de {x} + 3 * {y} * {x} - {y} e: {z}')

    '''exercicio 2'''
    num = int(input(f'Introduza a sua distanca em KMS'))
    num2 = int(input(f'introdza a o numero em minutos'))
    mts = num * 1000
    horas = num2 / 60
    segundos = num2 * 60
    print(f'Media em km/h {num / horas}')
    print(f'Media em m/s {mts / segundos}')

    '''exercico 3'''

    num = int(input(f'Introduza um número em segundos'))
    print(f'Os segundos introduzidos correspondem a {num / 86400} dias')

    '''Exercico 4'''
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

    '''exercicio 6'''
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

    '''exercicio 7'''