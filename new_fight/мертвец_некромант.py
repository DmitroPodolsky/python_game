import hero
from random import randint
import серая_мантия
import fight
import архив_монстов
import письма
name='мертвец_некромант'
a=150
b=8
c=12
zet=0
def first_ability():
    fight.u1=2
    global a
    print('поглощение урона')
    print(f'{a}+{fight.yan}={a + fight.yan}')
    a+= fight.yan
    fight.yan=0
    return randint(0,b)
def second_ability():
    fight.u2=2
    print('поглощение щита в урон')
    n=randint(b,b*2)
    print(f'{n}+{fight.der}={n + fight.der}')
    n+= fight.der
    fight.der=0
    return n
def third_ability():
    global a,zet,b,c
    if zet==0:
        print('ты так просто меня не убьешь!!!')
        a=50
        fight.yan=0
        zet=1
        b=20
        c=15
        return 0
    else:
        s=randint(1,2)
        if s==1:
            print('игнор брони')
            fight.der=0
            return randint(b,b*2)
        elif s==2:
            print('игнор урон,удар щитом')
            fight.yan=0
            return randint(0,c)
def death():
    hero.l+=25
    hero.con+=16
    c=randint(1,2)
    архив_монстов.h1 += 1
    if c==2:
        print('поздравляю вам выпала серая_мантия-можете заглянуть в инвентарь')
        серая_мантия.accept=0
    k = randint(1,4)
    if k == 1 and письма.nekromant_1 != 1:
        print('Получено новое письмо: "ваш долг"')
        письма.nekromant_1 = 1
    elif k == 3 and письма.nekromant_2 != 1:
        print('Получено новое письмо: "х"')
        письма.nekromant_2 = 1