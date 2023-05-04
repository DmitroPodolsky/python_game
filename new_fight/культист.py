import hero
from random import randint
import fight
import архив_монстов
import письма
name='культист'
a=250
b=20
c=20
may=0
def first_ability():
    global may
    global b
    if may>=4:
        fight.u1=4
        print('ритуальный удар')
        print(f'{hero.a}-{b*2}={hero.a-b*2} and {hero.c}-5={hero.c-5} and {hero.b}-5={hero.b-5}')
        hero.a-=b*2
        hero.b-=5
        hero.c-=5
        if hero.b<=0:
            hero.b=15
        if hero.c<=0:
            hero.c=15
        may=0
        return 0
    may+=1
    print(f'{may}/4 до ритуала')
    return randint(5,b)
def second_ability():
    global may,a,b,c
    fight.u2=3
    print('жертво-приношение')
    print(f'{a}-30={a - 30} and {c}+2={c + 2} and {b}+5={b + 5}')
    a-=30
    b+=5
    c+=2
    if may>=4:
        fight.u1=4
        print('ритуальный удар')
        print(f'{hero.a}-{b*2}={hero.a-b*2} and {hero.c}-5={hero.c-5} and {hero.b}-5={hero.b-5}')
        hero.a-=b*2
        hero.b-=5
        hero.c-=5
        if hero.b<=0:
            hero.b=15
        if hero.c<=0:
            hero.c=15
        may=0
        return 0
    may+=1
    print(f'{may}/4 до ритуала')
    return randint(10,b)
def third_ability():
    global may,a,b
    fight.u3=4
    print('поклонение ордену')
    print(f'{a}+30={a + 30}')
    a+=30
    if may>=4:
        fight.u1=4
        print('ритуальный удар')
        print(f'{hero.a}-{b*2}={hero.a-b*2} and {hero.c}-5={hero.c-5} and {hero.b}-5={hero.b-5}')
        hero.a-=b*2
        hero.b-=5
        hero.c-=5
        if hero.b<=0:
            hero.b=15
        if hero.c<=0:
            hero.c=15
        may=0
        return 0
    may+=1
    print(f'{may}/4 до ритуала')
    return randint(10,b)

def death():
    архив_монстов.d3 += 1
    hero.l += 25
    hero.con += 16
    k = randint(1,2)
    if k == 1 and письма.kultist != 1:
        print('Получено новое письмо: "доклад ордену"')
        письма.kultist = 1