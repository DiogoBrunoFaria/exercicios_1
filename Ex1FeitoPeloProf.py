"""
Declare uma lista para guardar as vendas do grupo central
Declara uma lista para guardar os nomes das cinco ilhas do grupo central
Peça dados ao utilizador e guarde-os na lista
Após o utilizador ter inserido os 5 valores apresente:
- Total das vendas
- O menor valor inserido
- O maior valor inserido
- A média das vendas
"""

ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']


if __name__ == '__main__':  # isto é o ponto de partida
    vendas = []
    for ilha in ilhas:
        vendas.append(float(input(f'insira as vendas para {ilha}')))
    print(f'vendas={vendas}')

    x = 0
    while x < len(ilhas):
        vendas.append(float(input(f'Insira as vendas para {ilhas[x]}')))
        x += 1
        print(f'Vendas={vendas}')

