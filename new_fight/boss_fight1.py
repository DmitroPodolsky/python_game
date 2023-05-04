import ведьма
import hero
from random import randint
from end_game import END_GAME
yan = 0
der = 0
den = 0
i1,i2,i3,i4=0,0,0,0
n=0
v=0
a=30000
name='Ведьма'
h=0
def end():
    global yan, der, den, i1, i2, i3, i4, n, v, a,h
    f = 0
    hero.a = 1000
    hero.b=1000
    hero.c=0
    print("""'a' - удар мечом\n'w' - уклонение от удара(перезарядка 4 хода)\n'd' - уклонение от удара(перезарядка 3 хода)\n's' - уклонение от удара(перезарядка 2 хода)\n'pass'-пропустить ход""")
    print()
    while hero.a > 0 and a > 0:
        w = input('Ваш ход - a, w, d or s: \nВвод: ')
        h=w
        print()
        der = randint(0, hero.c)
        if w == 'a':
            if i4>0:
                print(f'до окончания перезарядки остался {i4} хода ')
                continue
            yan = 1000
        elif w == 'w':
            if i1>0:
                print(f'до окончания перезарядки остался {i1} хода ')
                continue
            yan = hero.fort_ability()
            i1 = 4
        elif w == 'd':
            if i2>0:
                print(f'до окончания перезарядки остался {i2} хода ')
                continue
            yan = hero.fort_ability()
            i2 = 3
        elif w == 's':
            if i3>0:
                print(f'до окончания перезарядки остался {i3} хода ')
                continue
            yan = hero.fort_ability()

        elif w == 'pass':
            yan = 0
        else:
            print('Вводите правильно данные!')
            continue
        if a<=15000 and f==0:
            print('ты доигрался урод!!!')
            ведьма.v = 1
            a=30000
            hero.a+=300
            ведьма.x=0
            ведьма.f=0
            f=1
            yan=0
        if ведьма.v == 0 and ведьма.x==0:
            g = ведьма.first_ability()
        elif ведьма.v == 1 and ведьма.x==0:
            g = ведьма.first_ability1()
        elif ведьма.v == 0 and ведьма.x==1:
            g = ведьма.second_ability()
        elif ведьма.v == 1 and ведьма.x==1:
            g = ведьма.second_ability1()
        elif ведьма.v == 0 and ведьма.x==2:
            g = ведьма.third_ability()
        elif ведьма.v == 1 and ведьма.x==2:
            g = ведьма.third_ability1()
        if hero.kal == 'dodge':
            hero.kal = 'attack'
            yan = 0
            den = 0
            g = 0
            der = 0
        if g < der:
            print(f'{hero.ran} deffend attack')
            g = 0
            der = 0
        if yan < den:
            print(f'{name} deffend attack')
            yan = 0
            den = 0
        print(
            f'''Step:{n} - ваше здоровье: {hero.a}-{g}+{der}={hero.a - (g - der)}, 
            здоровье {name} : {a}-{yan}+{den}={a - (yan - den)}''')
        print()
        hero.a = hero.a - (g - der)
        a = a - (yan - den)
        i1 -= 1
        i2 -= 1
        i3 -= 1
        i4 -= 1
        n+=1
    if hero.a <= 0:
        print("Азриель был слишком слаб для неё и он погиб, но на этот раз граф обрёл действильный покой от своего тела и может пойти на небеса со своим сыном...")
        print("сама же империя вместе с остальным миром окунулась в епоху забытия,"
              " когда разруха и выживание всё на что надеються выжившие, но вскоре их борьба за выживание закончиться...")
        g=input()
        print("получено достижение:'отец и сын'")
        n=input()
        END_GAME()
    ведьма.death()
    return END_GAME()