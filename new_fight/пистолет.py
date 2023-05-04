from random import randint
import hero
import fight

a=45
b=10
c=18
accept = 1
def ability():
    c=randint(1,3)
    fight.der = 100000
    if c == 1:
        print('perfect shot')
        return randint(hero.b,hero.b+20)
    elif c == 2:
        fight.i1 = 3
        print('попадение')
        return randint(0,hero.b)
    elif c == 3:
        fight.i1=3
        print('промах')
        return 0