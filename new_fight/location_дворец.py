from random import randint
from культист import a as hp, b as damage, c as defense
from живая_плоть import a as hp1, b as damage1, c as defense1
from страж import a as hp2, b as damage2, c as defense2
import main_game


def v():
    main_game.a = 4
    a = randint(1, 3)
    if a == 1:
        print(f'Вам попался противник - культист\nhp - {hp}\ndamage - {damage}\ndefense - {defense}\n')
        return 1
    elif a == 2:
        print(f'Вам попался противник - живая_плоть\nhp - {hp1}\ndamage - {damage1}\ndefense - {defense1}\n')
        return 2
    elif a == 3:
        print(f'Вам попался противник - страж\nhp - {hp2}\ndamage - {damage2}\ndefense - {defense2}\n')
        return 3