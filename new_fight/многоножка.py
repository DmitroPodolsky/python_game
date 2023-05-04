import hero
from random import randint
import fight
import архив_монстов
import письма
name='многоножка'
a=200
b=2
c=10
def first_ability():
    fight.u2=2
    print('27 ударов подряд!')
    n=sum([randint(0,b) for i in range(27)])
    return n
def second_ability():
    r=randint(1,3)
    if r==2:
        print('захват-нету защиты и атаки в теченее хода')
        fight.yan=0
        fight.der=0
        fight.u2=3
        return 20
    else:
        print('промах захвата')
        return 5
def third_ability():
    global a,b
    fight.u3=2
    if a>20:
        print(f'{a}-20={a-20} and dmg +1')
        a-=20
        b+=1
        return b
    else:
        print(f'{a}+40={a + 40}')
        a+=40
        return b
def death():
    архив_монстов.h2 += 1
    hero.l+=25
    hero.con+=16
    k = randint(1,2)
    if k == 1 and письма.mnogonog != 1:
        print('Получено новое письмо: "отряд инквизиторов"')
        письма.mnogonog = 1