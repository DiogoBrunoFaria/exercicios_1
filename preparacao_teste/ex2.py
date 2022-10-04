"""
Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em Km) e o tempo necessário para a percorrer (em
minutos), e calcula a velocidade média em:
(a) Km / h
(b) m/s
"""
if __name__ == '__main__':
    num = int(input(f'Introduza a sua distanca em KMS'))
    num2 = int(input(f'introdza a o numero em minutos'))
    mts = num * 1000
    horas = num2 / 60
    segundos = num2 * 60
    print(f'Media em km/h {num / horas}')
    print(f'Media em m/s {mts / segundos}')
