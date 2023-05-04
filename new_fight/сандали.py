from random import randint
import hero
import fight

a=15 #hp+
b=7 #dmg+
c=8 #defense+
accept=1
def ability():
    print('Сальвадорський удар-перезарядка два хода')
    fight.i2 = 2
    return randint(0,hero.b*2)