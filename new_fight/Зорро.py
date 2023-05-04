import unique_fight
import hero
from random import randint
import пистолет
a=1000
b=55
c=0
v=0
g=0
x=0
f=0
drot2=0
def first_ability():
    global g,x,f
    if g == 'ближний':
        if f==0:
            f+=1
            if hero.kal=='dodge':
                return 0
            else:
                return b
        else:
            if f//3==1:
                x=1
                f=0
                if hero.kal == 'dodge':
                    return 0
                else:
                    return b
            elif f//2==1:
                f += 1
                if unique_fight.yan==0:
                    print('переиграл вора')
                    unique_fight.yan=b
                    return 0
                else:
                    print('воровской удар(обратно возвращает ваш урон)')
                    return unique_fight.yan
            else:
                f += 1
                return 0
    elif g == 'дальний':
        if f==1:
            f=0
            x=1
            unique_fight.yan = 0
            if hero.kal=='dodge':
                return 0
            else:
                d = randint(1, 3)
                print('выстрел')
                if d == 1:
                    print('perfect shot')
                    return randint(b, b * 2)
                elif d == 2:
                    print('попадение')
                    return b
                elif d == 3:
                    print('промах')
                    return 0
        else:
            f += 1
            unique_fight.yan=0
            return 0
def second_ability():
    global g, x, f
    if g == 'ближний':
        print('он поменял оружие')
        g='дальний'
        x=0
        return 20
    elif g == 'дальний':
        print('он поменял оружие')
        g='ближний'
        x=0
        return 20
def death():
    global drot2
    hero.l+=50
    hero.con+=60
    пистолет.accept=0
    print('вы получили пистолет(посмотрите в инвентаре)')
    drot2=1