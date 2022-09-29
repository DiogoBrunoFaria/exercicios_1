"""
lista com 5 casas
lista que gera numeros entre 1-50
maquina de numeros aleatorios
"""
import random


def gerador(ini, fim):
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':

    nums = [0, 0, 0, 0, 0]
    bonus = [0, 0]
    for x in range(len(nums)):
        while True:
            onumero = gerador(1, 50)
            if onumero not in nums:
                nums[x] = onumero
                break
    print(f'Numeros = {nums}')
    for x in range(len(bonus)):
        while True:
            onumero = gerador(1, 12)
            if onumero not in bonus:
                bonus[x] = onumero
                break
    print(f'bonus = {bonus}')
