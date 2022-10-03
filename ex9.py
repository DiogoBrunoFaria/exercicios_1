"""
primeiro ex
"""

if __name__ == '__main__':
    x = int(input(f'Escreva o primeiro numero '))
    y = int(input(f'Escreva o segundo numero '))
    z = (x + 3 * y) * (x - y)
    print(f'O valor de {x + 3 * y} * {x - y} e: {z}')

"""
segundo ex
"""
tamanho = input(f'Quantos numeros quer incerir?')
listaKM = [int(input(tamanho)) for c in range(5)]
listaM = []
print(listaKM)
