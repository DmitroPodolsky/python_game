import hero
from random import randint
import fight
import архив_монстов
import письма
name='страж'
a=150
b=40
c=40
zen=0
def first_ability():
    global zen
    if zen==2:
        zen=0
        print('получай подлец!!!')
        return randint(b,b*2)
    zen+=1
    return randint(0,b)
def second_ability():
    fight.u2=2
    if c>fight.yan:
        print('отражение удара')
        f=fight.yan
        fight.yan=0
        return f
    else:
        fight.den=c
        print('ты ещё получишь!!')
        print(f'{c}+10={c+10}')
        return 0
def third_ability():
    global c,b
    fight.u3=2
    if c>=20:
        print('броню в урон')
        print(f'{c}-20={c-20} and {b}+10={b+10}')
        c-=20
        b+=10
        return randint(0,b)
    else:
        print('урон в броню')
        print(f'{c}+20={c + 20} and {b}-10={b - 10}')
        c += 20
        b -= 10
        return randint(0, b)
def death():
    архив_монстов.d3 += 1
    hero.l+=25
    hero.con+=16
    k = randint(1,2)
    if k == 2 and письма.strag != 0:
        print('Получено новое письмо: "приказ"')
        письма.strag = 1