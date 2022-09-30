def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == '__main__':
    num = int(input("Incira um numero para vermos o seu faturial:  "))
    print(factorial(num))
    """
    resultado = 1
    contador = 1
    while contador <= num:
        resultado *= contador
        contador += 1
    print(resultado)
    """

