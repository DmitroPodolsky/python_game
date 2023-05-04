from random import randint
import hero
import fight

a = 20  # hp +
b = 4  # damage +
c = 6  # armor +
accept = 1


def ability():
    if hero.c>=2:
        print(f'{hero.c}-2={hero.c-2} and dmg plus half')
        hero.c-=2
        fight.i2 = 2
        return randint(hero.b//2,hero.b+hero.b//2)
    else:
        print(f'{hero.c}+6={hero.c+6}')
        hero.c=6
        fight.i2 = 2
        return 0