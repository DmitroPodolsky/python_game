import hero
from random import randint
import fight
import архив_монстов
import письма
name='живая_плоть'
a=400
b=10
c=0
def first_ability():
    global a
    if a>=200:
        print('перекат(игнорирует щит)')
        fight.der=0
        return randint(b,b*2)
    else:
        fight.u1=4
        print('кровавый перекат(игнорирует щит)')
        fight.der=0
        l = randint(b, b * 2)
        print(f'{hero.a}-{l}={hero.a-l}')
        hero.a-=l
        l = randint(b, b * 2)
        print(f'{hero.a}-{l}={hero.a - l}')
        hero.a -= l
        l = randint(b, b * 2)
        print(f'{hero.a}-{l}={hero.a - l}')
        hero.a -= l
        return 0
def second_ability():
    global a
    global c
    if a >= 200:
        print('щит из кусков тела')
        print(f'{c}+10={c+10}')
        c+=10
        return 0
    else:
        if c>=5:
            print('щит в атаку!')
            print(f'{c}-5={c - 5}')
            c-=5
            return c
        else:
            print('щит из кусков тела')
            print(f'{c}+8={c + 8}')
            c += 8
            return randint(0,b)
def third_ability():
    global b
    global a
    if a>=200:
        if a<=300:
            fight.u3=2
            print('закладки жира')
            print(f'{a}+40={a + 40}')
            a+=40
            return randint(0,b)
        else:
            print('кровь мутирует')
            print(f'{b}+3={b + 3}')
            b+=3
            return 0
    else:
        print('кровь прогрессирует')
        print(f'{b}+6={b + 6}')
        b+=6
        return b//2
def death():
    архив_монстов.d2 += 1
    hero.l+=25
    hero.con+=16
    k = randint(1,6)
    if k == 1 and письма.live_body_1 != 1:
        print('Получено новое письмо: "Лермонту"')
        письма.live_body_1 = 1
    elif k == 3 and письма.live_body_2 != 1:
        print('Получено новое письмо: "выезд"')
        письма.live_body_2 = 1
    elif k == 6 and письма.live_body_3 != 1:
        print('Получено новое письмо: "прощание"')
        письма.live_body_3 = 1