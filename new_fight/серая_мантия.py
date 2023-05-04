from random import randint
import hero
import fight

a=27
b=1
c=8
zet=0
accept = 1
def ability():
    global zet
    if zet==0:
        print('1/3 до магического удара')
        zet=1
        return randint(b, 10)
    elif zet==1:
        print('2/3 до магического удара')
        zet = 2
        return randint(b,10)
    elif zet==2:
        print('магический удар!!! перезарядка три хода')
        zet = 0
        fight.i1=2
        return hero.b*2