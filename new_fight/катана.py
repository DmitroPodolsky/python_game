from random import randint
import hero
import fight

a=35
b=20
c=10
accept = 1
def ability():
    if hero.a<=100:
        print('отчаянный удар')
        return hero.b
    else:
        fight.i4=2
        print('двойной выпад')
        return randint(0,b)+randint(0,hero.b)