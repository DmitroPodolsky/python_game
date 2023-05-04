import hero
from random import randint
import fight
import письма
import архив_монстов
name='оживший_скелет'
a=100
b=25
c=0
def first_ability():
    global a
    if a+40>100:
        print(f'hp={a} and dmg+{(a+40)-100}')
        w=randint(0,b)
        f=randint(0,a+40-100)
        a=100
        return w+f
    else:
        print(f'{a}+40={a + 40}')
        a+=40
        return randint(0,b)
def second_ability():
    print('обратный удар')
    return fight.yan
def third_ability():
    fight.u3=999
    global a
    print('вторая жизнь')
    fight.yan=0
    a=100
    return 0
def death():
    hero.l+=25
    hero.con+=16
    архив_монстов.h3+=1
    k = randint(1,4)
    if k == 2 and письма.skelet_1 != 1:
        print('Получено новое письмо: "задача"')
        письма.skelet_1 = 1
    elif k == 4 and письма.skelet_2 != 1:
        print('Получено новое письмо: "зет"')
        письма.skelet_2 = 1