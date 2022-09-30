"""
pede ao utilizador os seguintes dados
-BI
-Nome
_Morada
-Codigo Postal
-Custo Hora
-Ano de Nascimento
"""
pessoa = (1, 'Maria', {'morada': 'rua de cima, 1', 'cp': 9500}, 12.50)
#exemplo de um set
meses={'janeiro', 'fevereiro', 'março'}

if __name__ == '__main__':
    """
    print(pessoa[2].keys())  # imprime os titelos
    print(pessoa[2].values())  # imprime as respostas dos titelos
    print()

    for k in pessoa[2].keys():
        print(k)
    print()
    for v in pessoa[2].values():
        print(v)
    print()
    for k in pessoa[2].keys():
        print(f'{k} = {pessoa[2][k]}')
    """
    print(meses.add('Abril'))
    # print(meses)
    # meses.pop()
    # print(meses)
