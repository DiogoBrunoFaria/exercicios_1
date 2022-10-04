"""
Escreva um programa em Python que lê uma sequência de dígitos, sendo
cada um dos dígitos fornecido numa linha separada, e calcula o número
inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
sequência de dígitos é fornecido ao programa o inteiro
1. O seu programa
deve permitir a interação:
Escreva um dígito
(-1 para terminar)
? 3
Escreva um dígito
(-1 para terminar)
? 2
Escreva um dígito
(-1 para terminar)
? 5
Escreva um dígito
(-1 para terminar)
? 7
Escreva um dígito
(-1 para terminar)
? -1
O número é: 3257
"""
if __name__ == '__main__':
    list_valor = []
    while True:
        try:

            valor = int(input(f'insira um inteiro para terminar utiliza -1'))
            if valor < 0:
                break
            list_valor.append(valor)
            print(list_valor)

        except ValueError:
            print('Digite um valor válido')
    valor = ''
    for x in range(len(list_valor)):
        valor += str(list_valor[x])

    print(f'O numero é: {valor}')
