"""
Escreva um programa em Python que calcula o valor da soma.

para um dado valor de x e de n. O seu programa deve ter em atenção
que o i-ésimo termo da soma pode ser obtido do termo na posição i
1,
multiplicando-o por x/i. O seu programa deve permitir a interação:

12 CAPÍTULO 2. ELEMENTOS BÁSICOS DE PROGRAMAÇÃO
Qual o valor de x
? 2
Qual o valor de n
? 3
O valor da soma é 6.333333333333333
"""
if __name__ == '__main__':
    while True:
        try:
            x = int(input('Qual o valor de x: '))
            n = int(input('Qual o valor de n: '))

            soma = 1 + x
            for z in range(2, n + 1):
                soma += (x ** z) / z

            print(soma)

            continuar = input('Repetir (s | n)? ')
            if continuar == 'n':
                break

        except ValueError:
            print('Digite um valor válido')

    print(f'Adeus!')
