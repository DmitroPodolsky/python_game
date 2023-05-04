import Аластор,Зорро,Приосвященство,Отшельник
import main_game
import hero
import text
from random import randint
from importlib import reload
import архив_монстов
from end_game import END_GAME
yan = 0
der = 0
den = 0
i1,i2,i3,i4=0,0,0,0
n=0
v=0
def doss(b,name,a):
    global yan,der,den,i1,i2,i3,i4,n,v
    print(f'{text.a} vs {name}')
    print()
    print("""'a' - удар мечом\n'w' - ход бронёй\n'd' - ход сапогами\n's' - уклонение от удара\n'pass'-пропустить ход""")
    print()
    ll=0
    while hero.a > 0 and a > 0:
        w = input('Ваш ход - a, w, d or s: \nВвод: ')
        print()
        der = randint(0, hero.c)
        if w == 'a':
            if i4 > 0:
                print(f'до окончания перезарядки остался {i4} хода ')
                continue
            yan = hero.first_ability()
        elif w == 'w':
            if i1 > 0:
                print(f'до окончания перезарядки остался {i1} хода ')
                continue
            yan = hero.second_ability()
        elif w == 'd':
            if i2 > 0:
                print(f'до окончания перезарядки остался {i2} хода ')
                continue
            yan = hero.third_ability()
        elif w == 's':
            if i3 > 0:
                print(f'до окончания перезарядки остался {i3} хода ')
                continue
            yan = hero.fort_ability()
            i3 = 2
        elif w == 'pass':
            yan = 0
        else:
            print('Вводите правильно данные!')
            continue
        if b==1:
            if Отшельник.x==0:
                g=Отшельник.first_ability()
            elif Отшельник.x==1:
                g=Отшельник.second_ability()
            elif Отшельник.x==2:
                g=Отшельник.third_ability()
        elif b==2:
            if Зорро.v==0:
                Зорро.v=1
                e=randint(1,2)
                if e==1:
                    print('он достал нож')
                    Зорро.g = 'ближний'
                    g=0
                elif e==2:
                    print('вижу пистолет его')
                    Зорро.g = 'дальний'
                    g=0
            elif Зорро.x==0:
                g=Зорро.first_ability()
            elif Зорро.x==1:
                g=Зорро.second_ability()
        elif b==3:
            a=input('назови мне пароль: ')
            if a=='':
                print('значит ты всё-таки убил её(я не могу говорить),это меняет дело, значит ты знаешь историю графа.'
                      'Впечетляюще,ты хочешь спасти мир, а я хочу закончить свои путешествия во времени...')
                a=input()
                print("его посох загоредся алым пламенем и начал чертить различные знаки")
                a = input()
                print("ты вселишся в это тело, а я тебя встречу там уже, мы отправляемся 1940-ые, это время когда мы можем всё изменить")
                a = input()
                print("из неоткуда вытащил труп из портала и дальше я почуствовал лёгкий огонёк по телу.")
                a=input()
                a = 0
                g = 0
                return END_GAME()
            else:
                print('ты не из этой линии,ты мне не нужен...')
                g=0
                a=0
        elif b==4:
            if a<=500 and v==0:
                print('Во славу Ордена!!!')
                a=1000
                v=1
            if ll==1:
                ll=0
                print('я тебя заставлю помучиться')
            elif Приосвященство.x==0:
                g=Приосвященство.first_ability()
            elif Приосвященство.x==1:
                g=Приосвященство.second_ability()
            elif Приосвященство.x==2:
                g=Приосвященство.third_ability()
        n += 1
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
    if hero.a <= 0:
        print('''Вы погибли,ваше снаряжение сохранилось и находиться в инвентаре, но ваши души съели монстры,
также ваш уровень понижен на иденицу''')
        if main_game.level > 0:
            main_game.level -= 1
            hero.b0-=2
            hero.a0-=5
            hero.a -= 5
            hero.b -= 2
            hero.l0-=10
        hero.c = hero.c0 + hero.c1 + hero.c2 + hero.c3
        hero.b = hero.b0 + hero.b1 + hero.b2 + hero.b3
        hero.a = hero.a0 + hero.a1 + hero.a2 + hero.a3
        hero.con=10
        reload(Отшельник)
        reload(Зорро)
        reload(Приосвященство)
        reload(Аластор)
        main_game.tank()
        return main_game.tank()
    else:
        if b == 1:
            архив_монстов.b = 1
            Отшельник.death()
        elif b == 2:
            архив_монстов.p=1
            Зорро.death()
        elif b == 3:
            Аластор.death()
        elif b == 4:
            архив_монстов.d = 1
            Приосвященство.death()
        if архив_монстов.b == 1:
            print('вы вспомнили 14-ый фрагмент памяти')
        if архив_монстов.p == 1:
            print('вы вспомнили 15-ый фрагмент памяти')
        if архив_монстов.d == 1:
            print('вы вспомнили 16-ый фрагмент памяти')
        print('win')
        return main_game.tank()