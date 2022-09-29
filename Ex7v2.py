"""
Declare uma lista para guardar as vendas de gasolina e gas´´eo no grupo oriental
Apresente:
- Total das vendas
- O total de vendas de gasolina
- O total de vendas de gasóleo
- O total de vendas para cada ilha
Exemplo da estrutura de armazenamento das vendas:
    vendas = [
         TER PIC  FAI  GRA  SJR
        [10, 20 , 30, 40 , 50], #Gasolina
        [15, 25, 35, 45, 55]    #Gasoleo
    ]
    ou então:
    vendas = [
         Gasoleo
          |  Gasolina
        [10, 15], TER
        [20, 25], PIC
        [30, 35], FAI
        [40, 45], GRA
        [50, 55]  SJR
    ]
"""
if __name__ == '__main__':
    ilhas = ['Terceira', 'Graciosa', 'Pico', 'Faial', 'São Jorge']
    tipos = ['Gasolina', 'Gasoleo']
    vendas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
if __name__ == '__main__':
    # ober input
    for x in range(len(vendas)):
        for y in range(len(vendas[x])):
            while True:
                try:
                    vendas[x][y] = int(input(f'Insira vendas de {tipos[x]} para ilha {ilhas[y]}: '))
                    break
                except ValueError:
                    print(f'Insira um Valor valido para vendas de {tipos[x]} na ilha {ilhas[y]}')
        print(vendas)

    # Imprimir vendas por tipo
    for x in range(len(vendas)):
        total = 0
        for y in range(len(vendas[x])):
            total += vendas[x][y]
        print(f'Total de vendas {tipos[x]} = {total}')

    # Imprimir vendas por ilha

    """
    total_vendas = 0
    for x in range(5):
        total_linha = 0
        for y in range(2):
            print(f'vendas [{y}] [{x}] = {vendas[y][x]}')
            total_vendas = total_vendas + vendas[y][x]
            total_linha = total_vendas + vendas[y][x]
        print(f'Total de linhas: {total_linha}')
    print(f'Total de vendas: {total_vendas}')

    total = 0
    for y in range(5):
        for x in range(2):
            print(f'x={x} y={y}')
            total = total + vendas[x][y]
        print(total)
        """
