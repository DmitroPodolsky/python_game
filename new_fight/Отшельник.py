import unique_fight
import hero
from random import randint
import катана
a=1000
b=10
c=0
zen=0
f=0
x=0
drot1=0
def first_ability():
    global f,zen,x
    if zen==5:
        print('прочитан')
        print(f'{hero.a}-9999={hero.a-9999}')
        hero.a-=9999
        return 0
    if f==0:
        f+=1
        if hero.kal=='dodge':
            return 0
        else:
            zen+=1
            print(f'{zen}/5')
            return b
    else:
        if f//3==1:
            if hero.kal == 'dodge':
                f=0
                x=1
                return 0
            else:
                f=0
                x=1
                zen += 1
                print(f'{zen}/5')
                return b
        else:
            a=randint(1,3)
            if a==2:
                print('уклонился')
                f+=1
                unique_fight.yan=0
                return 0
            else:
                f+=1
                return 0
def second_ability():
    global f, zen, x
    if zen==5:
        print('прочитан')
        print(f'{hero.a}-9999={hero.a-9999}')
        hero.a-=9999
        return 0
    if f==0:
        if unique_fight.yan==0:
            f+=1
            return 0
        else:
            f+=1
            zen+=1
            print(f'{zen}/5')
            return b
    else:
        if f//4==1:
            f=0
            if hero.kal=='dodge':
                x=2
                return 0
            else:
                x=2
                zen+=1
                print(f'{zen}/5')
                return b
        else:
            f+=1
            return 0
def third_ability():
    global f, zen, x, drot1
    if zen==5:
        print('прочитан')
        print(f'{hero.a}-9999={hero.a-9999}')
        hero.a-=9999
        return 0
    if f==1:
        f=0
        if unique_fight.yan>0:
            print('заметил')
            x=0
            return 0
        else:
            print('засада')
            zen+=1
            x=0
            print(f'{zen}/5')
            return b
    else:
        print('я его не вижу')
        f+=1
        unique_fight.yan=0
        return 0
def death():
    global drot1
    hero.l+=50
    hero.con+=60
    катана.accept=0
    print('вы получили катану(посмотрите в инвентаре)')
    drot1 = 1

