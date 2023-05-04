import hero
from random import randint
import boss_fight1
b=25
v=0
x=0
f=0
g=0
def first_ability():
    global f,x,b
    if f==3:
        f=0
        x=1
        return 0
    else:
        f+=1
        if hero.kal=='dodge':
            return 0
        else:
            b+=25
            return b
def second_ability():
    global f, x, b
    if f==0:
        f+=1
        print('она готовит магические шары')
        return 0
    elif f==1:
        if boss_fight1.yan>0:
            print('шар взорвался')
            boss_fight1.yan=0
            b+=50
            f=0
            x=2
            return b
        else:
            f+=1
            return 0
    elif f==2:
        if boss_fight1.yan>0:
            print('шар прилетел обратно к врагу')
            boss_fight1.yan=2000
            f=0
            x=2
            return 0
        else:
            print('шар всю свою инергию на вас перевёл')
            f=0
            x=2
            hero.a-=150
            return 0
def third_ability():
    global f, x, b,g
    a = randint(1,2)
    if f==0:
        f+=1
        if a==1:
            g=1
            print('она достала два клинка')
            return 0
        elif a==2:
            g=2
            print('она взлетела на 2 метра и приготовила синие шары')
            return 0
    if g==1:
        if f==6:
            x=0
            f=0
            return 0
        elif f%2==1:
            f += 1
            return b
        else:
            f += 1
            return 0
    elif g==2:
        if f==5:
            x=0
            f=0
            return 0
        elif f%2==0:
            f += 1
            return b+50
        else:
            f += 1
            return 0
def first_ability1():
    global f, x, b
    if f==0:
        f+=1
        print('она превратилась в гигантское чудище(невосприимчева к урону)')
        print('сдохнииии')
        return 0
    if boss_fight1.yan>0:
        boss_fight1.yan=0
    if f!=3:
        f+=1
        return b
    else:
        x=1
        f=0
        return 0
def second_ability1():
    global f, x, b
    if boss_fight1.yan>0:
        boss_fight1.yan=0
    if f==0:
        print('её тело воспламенилось ярко-синем пламенем, она к чему-то готовиться')
        f+=1
        return 0
    elif f==1:
        f+=1
        return 0
    elif f==2:
        if boss_fight1.h == 'pass':
            print('она дунула на вас ярко-синим пламенем и ничего не сработало')
            print('*вы думаете ахуеть,сработало*')
            x=2
            f=0
            return 0
        else:
            print('она дунула на вас ярко-синим пламенем и вас снесло вместе с ним')
            f=0
            x=2
            return 250
def third_ability1():
    global f, x, b, g
    a = randint(1, 2)
    if f == 0:
        f += 1
        print('она потеряла свою чудовищную форму')
        if a == 1:
            g = 1
            print('она достала два клинка')
            return 0
        elif a == 2:
            g = 2
            print('она взлетела на 2 метра и приготовила синие шары')
            return 0
    if g == 1:
        if f == 10:
            x = 0
            f = 0
            return 0
        elif f % 2 == 1:
            f += 1
            return 100
        else:
            f += 1
            return 0
    elif g == 2:
        if f == 10:
            x = 0
            f = 0
            return 0
        elif f % 2 == 0:
            f += 1
            return 150
        else:
            f += 1
            return 0
def death():
    print('когда она снова сняла свою чудовищную форму Азриель ей занёс в грудь синий меч и она упала от бессилия')
    print("она: и думаешь ты победил малышь семидиселетний? ты нихера не изменил, лишь потянул время возрождение нашей империи")
    print("Азриель: её разрухи...")
    print("ты...(она начала создавать синий шар)")
    print("но тут же из неоткуда Аластор взмахом посоха буквально испепилил её")
    print("Аластор:щас тайм-лайм спадёт, слушай внимательно, в следующем тайм-лайне скажи мою любимую фразу:'время не щадит'")
    print('Азриель: что?')
    print('а от Алостора остался только посох уже...')
    r=input()
    print('на этот раз Азриель положил конец основателям этой заразы и культистам по всей империи, но ведьма была права что мог сделать жалкий старик за короткое время?')
    print("ответ-ничего,поэтому ничего не поменялось,мир погрузился в хаос, но на этот раз есть слабые отголоски человечества")
    o=input()
    print('получено достижение "начинающий в Dark Souls"')
    m=input()
