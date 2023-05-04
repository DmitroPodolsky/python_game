import hero
from random import randint
import сапог
import fight
import архив_монстов
import письма
name='путешественник'
a=200
b=4
c=10
def first_ability():
    return randint(0,b)
def second_ability():
    global a
    if a==200:
        return first_ability()
    elif a>=190:
        a=200
        return 0
    else:
        print(f'{a}+10={a+10}')
        a+=10
        return 0
def third_ability():
    global b
    fight.u3=3
    print(f'{b}*2={b*2}')
    b*=2
    return first_ability()
def death():
    hero.l+=25
    hero.con+=16
    c = randint(1,2)
    архив_монстов.h4 += 1
    if c==2:
        print('поздравляю вам выпала кирка - можете заглянуть в инвентарь')
        сапог.accept=0
    k = randint(1,2)
    if k == 1:
        if письма.traveler != 1:
            print('Получено новое письмо: "777"')
            письма.traveler = 1