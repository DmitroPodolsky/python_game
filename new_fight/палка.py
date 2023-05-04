from random import randint
import hero

a=10
b=10
c=5
accept=1
def ability():
    v=randint(1,4)
    if v==1:
        print('Двойной удар!')
        x = randint(0, hero.b)
        return x*2
    else:
        x = randint(0, hero.b)
    return x