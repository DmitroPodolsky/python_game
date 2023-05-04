import unique_fight
import hero
from random import randint
import сапоги_ордена
a=1000
b=25
c=0
zen=0
x=0
f=0
drot4=0
def first_ability():
    global f, zen, x
    if zen>=12:
        print('ты будешь долго мучаться')
        print(f'{hero.a}-1={hero.a-1}')
        hero.a-=1
        unique_fight.yan=0
        return 0
    if f==2:
        f=0
        x=randint(1,2)
        return 0
    else:
        if hero.kal=='dodge' or unique_fight.der==100000:
            f+=1
            return 0
        else:
            zen+=1
            print(f'{zen}/12')
            f+=1
            return b
def second_ability():
    global f, zen, x
    if zen >= 12:
        print('ты будешь долго мучаться')
        print(f'{hero.a}-1={hero.a - 1}')
        hero.a -= 1
        unique_fight.yan = 0
        return 0
    if f%2==1:
        f += 1
        return 0
    elif f==4:
        f=0
        x=randint(0,1)
        if x==1:
            x=2
        return 0
    else:
        if hero.kal == 'dodge' or unique_fight.der == 100000:
            f += 1
            return 0
        else:
            zen += 1
            print(f'{zen}/12')
            f += 1
            return b
def third_ability():
    global f, zen, x
    if zen >= 12:
        print('ты будешь долго мучаться')
        print(f'{hero.a}-1={hero.a - 1}')
        hero.a -= 1
        unique_fight.yan = 0
        return 0
    elif f==0:
        f+=1
        print('он что-то бормочет себе под нос, вижу ауру странную')
        return 0
    elif f==1:
        f+=1
        if unique_fight.der == 100000:
            print('ритуал провалился')
        else:
            print('ритуальный удар')
            zen+=4
            print(f'{zen}/12')
            return b
    elif f==3:
        f=0
        x=randint(0,1)
        return 0
    else:
        f+=1
        return 0
def death():
    global drot4
    hero.l+=50
    hero.con+=60
    сапоги_ордена.accept=0
    drot4=1
    print('вы получили сапоги_ордена(посмотрите в инвентаре)')