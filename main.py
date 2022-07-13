# Adivinhe o número

# O computador irá gerar um numero aleatorio para tentarmos adivinhas

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, número inserido é MENOR')
        elif guess > random_number:
            print('Desculpe, número inserido é MAIOR')

    print('Parabéns, você adivinhou corretamente')

guess(10)

