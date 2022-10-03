"""
primeiro ex
"""

if __name__ == '__main__':
    """
    x = int(input(f'Escreva o primeiro numero '))
    y = int(input(f'Escreva o segundo numero '))
    z = (x + 3 * y) * (x - y)
    print(f'O valor de {x + 3 * y} * {x - y} e: {z}')
    """
"""
segundo ex
"""

listaKM = [int(input()) for c in range(5)]
comp = listaKM.__len__()
mediaKM = sum(listaKM) / comp
print(f'A media em KM é de {mediaKM}')

listaM = [int(input()) for c in range(5)]
comp = listaKM.__len__()
mediaM = sum(listaKM) / comp
print(f'A media em M é de {mediaM}')

print(listaKM)
print(comp)
