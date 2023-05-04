import main_game
import hero
import text
from random import randint
from pi_болото import гнилой_мертвец, мерзкая_слизь, дикий_туземец
from pi_пустыня import песчанный_червь, разбойник, ядовитый_скорпион
from importlib import reload
import путешественник,мертвец_некромант,многоножка,оживший_скелет
import живая_плоть,культист,страж
import письма
import архив_монстов
n = 0
u1 = 0
u2 = 0
u3 = 0
yan = 0
der = 0
den = 0
i1,i2,i3,i4=0,0,0,0
def d(name, f, a):
    global yan
    global n
    global u1,i1
    global u2,i2
    global u3,i3,i4
    global der
    global den
    print(f'{text.a} vs {name}')
    u = 0
    hh = 0
    print()
    print("""'a' - удар мечом\n'w' - ход бронёй\n'd' - ход сапогами\n's' - уклонение от удара\n'pass'-пропустить ход""")
    print()
    while hero.a > 0 and a > 0:
        w = input('Ваш ход - a, w, d or s: \nВвод: ')
        print()
        der = randint(0, hero.c)
        if w == 'a':
            if i4>0:
                print(f'до окончания перезарядки остался {i4} хода ')
                continue
            yan = hero.first_ability()
        elif w == 'w':
            if i1>0:
                print(f'до окончания перезарядки остался {i1} хода ')
                continue
            yan = hero.second_ability()
        elif w == 'd':
            if i2>0:
                print(f'до окончания перезарядки остался {i2} хода ')
                continue
            yan = hero.third_ability()
        elif w == 's':
            if i3>0:
                print(f'до окончания перезарядки остался {i3} хода ')
                continue
            yan = hero.fort_ability()
            i3=2
        elif w == 'pass':
            yan = 0
        else:
            print('Вводите правильно данные!')
            continue
        if main_game.a == 1:
            if f == 1:
                мерзкая_слизь.a = a
                den = randint(0, мерзкая_слизь.c)
                s = randint(1, 2)
                if s == 1:
                    g = мерзкая_слизь.first_ability()
                elif s == 2:
                    if a < 100 and u <= 0:
                        g = мерзкая_слизь.second_ability()
                        u = 10
                    elif u <= 0:
                        g = мерзкая_слизь.first_ability()
                else:
                    g = 0
                a = мерзкая_слизь.a
            elif f == 2:
                den = randint(0, гнилой_мертвец.c)
                s = randint(1, 2)
                if s == 1:
                    if a <= round(гнилой_мертвец.a * 0.5) and u <= 0:
                        a = гнилой_мертвец.first_ability(a)
                        g = 0
                        u = 3
                    elif u <= 0:
                        g = гнилой_мертвец.first_ability(a)
                elif s == 2:
                    g = гнилой_мертвец.second_ability()
                else:
                    g = 0
            elif f == 3:
                den = randint(0, дикий_туземец.c)
                s = randint(1, 2)
                if s == 1:
                    g = дикий_туземец.first_ability(a)
                elif s == 2:
                    g = дикий_туземец.second_ability()
                else:
                    g = 0
        elif main_game.a == 2:
            if f == 1:
                песчанный_червь.a = a
                den = randint(0, песчанный_червь.c)
                s = randint(1, 2)
                if s == 1:
                    g = песчанный_червь.first_ability()
                elif s == 2:
                    g = песчанный_червь.second_ability()
                a = песчанный_червь.a
            elif f == 2:
                den = randint(0, разбойник.c)
                s = randint(1, 2)
                if s == 1:
                    if u <= 0:
                        g = разбойник.first_ability()
                        u = 3
                    else:
                        g = разбойник.second_ability()
                elif s == 2:
                    g = разбойник.second_ability()
                else:
                    g = 0
            elif f == 3:
                den = randint(0, ядовитый_скорпион.c)
                s = randint(1, 3)
                if s == 1:
                    if u <= 0:
                        g = ядовитый_скорпион.first_ability()
                        print(f'{hero.c}-1={hero.c - 1} and {hero.b}-1={hero.b - 1}')
                        if hero.c - 1 <= 0:
                            hero.c = 0
                        else:
                            hero.c -= 1
                        if hero.b - 1 == 0:
                            hero.b = 1
                        else:
                            hero.b -= 1
                        u = 5
                    else:
                        g = ядовитый_скорпион.second_ability()
                elif s == 2:
                    g = ядовитый_скорпион.second_ability()
                elif s == 3 and hh <= 0:
                    den, g = ядовитый_скорпион.third_ability(den)
                    hh = 3
                else:
                    g = 0
        elif main_game.a==3:
            if f==1:
                den = randint(0, многоножка.c)
                многоножка.a = a
                s = randint(1, 3)
                if s==1 and u1<=0:
                    g = многоножка.first_ability()
                elif s==2 and u2<=0:
                    g = многоножка.second_ability()
                elif s==3 and u3<=0:
                    g = многоножка.third_ability()
                else:
                    g=многоножка.b
                a=многоножка.a
            elif f==2:
                den = randint(0, оживший_скелет.c)
                оживший_скелет.a= a
                s = randint(1, 2)
                if a-yan<=0 and u3<=0:
                    g = оживший_скелет.third_ability()
                elif s == 1 and u1 <= 0:
                    g = оживший_скелет.first_ability()
                elif s == 2 and u2 <= 0:
                    g = оживший_скелет.second_ability()
                else:
                    g=0
                a = оживший_скелет.a
            elif f==3:
                den = randint(0, путешественник.c)
                путешественник.a = a
                s = randint(1, 3)
                if s == 1 and u1 <= 0:
                    g = путешественник.first_ability()
                elif s == 2 and u2 <= 0:
                    g = путешественник.second_ability()
                elif s == 3 and u3 <= 0:
                    g = путешественник.third_ability()
                else:
                    g = 0
                a = путешественник.a
            elif f==4:
                den = randint(0, мертвец_некромант.c)
                мертвец_некромант.a=a
                s = randint(1, 2)
                if a - yan <= 0 or мертвец_некромант.zet==1:
                    g = мертвец_некромант.third_ability()
                elif s == 1 and u1 <= 0:
                    g = мертвец_некромант.first_ability()
                elif s == 2 and u2 <= 0:
                    g = мертвец_некромант.second_ability()
                else:
                    g=0
                a=мертвец_некромант.a
        elif main_game.a==4:
            if f==1:
                den = randint(0, культист.c)
                культист.a = a
                s = randint(1, 3)
                if s == 1 and u1 <= 0:
                    g = культист.first_ability()
                elif s == 2 and u2 <= 0:
                    g = культист.second_ability()
                elif s == 3 and u3 <= 0:
                    g = культист.third_ability()
                    a = культист.a
                    g+=культист.second_ability()
                else:
                    g = randint(5,10)
                a = культист.a
            elif f==2:
                den = randint(0, живая_плоть.c)
                живая_плоть.a = a
                s = randint(1, 3)
                if s == 1 and u1 <= 0:
                    g = живая_плоть.first_ability()
                elif s == 2 and u2 <= 0:
                    g = живая_плоть.second_ability()
                elif s == 3 and u3 <= 0:
                    g = живая_плоть.third_ability()
                else:
                    g = живая_плоть.b
                a = живая_плоть.a
            elif f==3:
                den = randint(0, страж.c)
                страж.a = a
                s = randint(1, 3)
                if s == 1 and u1 <= 0:
                    g = страж.first_ability()
                elif s == 2 and u2 <= 0:
                    g = страж.second_ability()
                elif s == 3 and u3 <= 0:
                    g = страж.third_ability()
                else:
                    g = страж.first_ability()
                a = страж.a
        n += 1
        if hero.kal == 'dodge':
            hero.kal='attack'
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
        u -= 1
        u1-=1
        u2-=1
        u3-=1
        i1-=1
        i2-=1
        i3-=1
        i4-=1
        hh -= 1
    if hero.a <= 0:
        print('''Вы погибли,ваше снаряжение сохранилось и находиться в инвентаре, но ваши души съели монстры,
также ваш уровень понижен на иденицу''')
        reload(мерзкая_слизь)
        reload(гнилой_мертвец)
        reload(дикий_туземец)
        reload(ядовитый_скорпион)
        reload(песчанный_червь)
        reload(разбойник)
        reload(многоножка)
        reload(мертвец_некромант)
        reload(путешественник)
        reload(оживший_скелет)
        reload(культист)
        reload(живая_плоть)
        reload(страж)
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
        main_game.tank()
    else:
        hero.i = 0
        hero.u = 0
        hero.c = hero.c0 + hero.c1 + hero.c2 + hero.c3
        hero.b = hero.b0 + hero.b1 + hero.b2 + hero.b3
        if hero.a>hero.a0 + hero.a1 + hero.a2 + hero.a3:
            hero.a=hero.a0 + hero.a1 + hero.a2 + hero.a3
        reload(мерзкая_слизь)
        reload(гнилой_мертвец)
        reload(дикий_туземец)
        reload(ядовитый_скорпион)
        reload(песчанный_червь)
        reload(разбойник)
        reload(многоножка)
        reload(мертвец_некромант)
        reload(путешественник)
        reload(оживший_скелет)
        reload(культист)
        reload(живая_плоть)
        reload(страж)
        if main_game.a == 1:
            if f == 1:
                hero.l, hero.con = мерзкая_слизь.death(hero.l, hero.con)
                k = randint(1, 2)
                архив_монстов.b3 += 1
                if k == 1:
                    if письма.sl != 1:
                        print('Получено новое письмо: "для Лермонта"')
                        письма.sl = 1
            elif f == 2:
                hero.l, hero.con = гнилой_мертвец.death(hero.l, hero.con)
                k = randint(1, 4)
                архив_монстов.b1 += 1
                if k == 2:
                    if письма.gn_1 != 1:
                        письма.gn_1 = 1
                        print('Вы получили новое письмо: Письмо "Р"')
                elif k == 4:
                    if письма.gn_2 != 1:
                        письма.gn_2 = 1
                        print('Получено новое письмо: "доклад"')
            elif f == 3:
                hero.l, hero.con = дикий_туземец.death(hero.l, hero.con)
                k = randint(1, 2)
                архив_монстов.b2 += 1
                if k == 1:
                    if письма.tusemec != 1:
                        письма.tusemec = 1
                        print('Получено новое письмо: "я"')
            elif main_game.a == 2:
                if f == 1:
                    hero.l, hero.con = песчанный_червь.death(hero.l, hero.con)
                    k = randint(1, 2)
                    архив_монстов.p1 += 1
                    if k == 2:
                        if письма.peschan != 1:
                            print('Получено новое письмо: "мед осмотр"')
                            письма.peschan = 1
                elif f == 2:
                    hero.l, hero.con = разбойник.death(hero.l, hero.con)
                    k = randint(1, 4)
                    архив_монстов.p2 += 1
                    if k == 1:
                        if письма.rasboy_1 != 1:
                            print('Получено новое письмо: "себе"')
                            письма.rasboy_1 = 1
                    elif k == 3:
                        if письма.rasboy_2 != 1:
                            print('Получено новое письмо: "доклад2"')
                            письма.rasboy_2 = 1
                elif f == 3:
                    hero.l, hero.con = ядовитый_скорпион.death(hero.l, hero.con)
                    k = randint(1, 2)
                    архив_монстов.p3 += 1
                    if k == 1:
                        if письма.scorpion != 1:
                            print('Получено новое письмо: "императору"')
                            письма.scorpion = 1
        elif main_game.a==3:
            if f==1:
                многоножка.death()
            elif f == 2:
                оживший_скелет.death()
            elif f == 3:
                путешественник.death()
            elif f == 4:
                мертвец_некромант.death()
        elif main_game.a == 4:
            if f == 1:
                культист.death()
            elif f == 2:
                живая_плоть.death()
            elif f == 3:
                страж.death()
        if hero.l >= hero.l0:
            main_game.level += 1
            print(f'Поздравление! У вас новый уровень {hero.ran} - {main_game.level} and hp+5 ,dmg+2')
            hero.l -= hero.l0
            hero.l0 += 10
            hero.a += 5
            hero.a0 += 5
            hero.b += 2
            hero.b0 += 2
        if архив_монстов.b1 == 3:
            архив_монстов.b1+=1
            print('вы вспомнили 1-ый фрагмент памяти')
        if архив_монстов.b2 == 3:
            архив_монстов.b2 += 1
            print('вы вспомнили 2-ый фрагмент памяти')
        if архив_монстов.b3 == 3:
            архив_монстов.b3 += 1
            print('вы вспомнили 3-ый фрагмент памяти')
        if архив_монстов.p1 == 3:
            архив_монстов.p1 += 1
            print('вы вспомнили 4-ый фрагмент памяти')
        if архив_монстов.p2 == 3:
            архив_монстов.p2 += 1
            print('вы вспомнили 5-ый фрагмент памяти')
        if архив_монстов.p3 == 3:
            архив_монстов.p3 += 1
            print('вы вспомнили 6-ый фрагмент памяти')
        if архив_монстов.h1 == 3:
            архив_монстов.h1 += 1
            print('вы вспомнили 7-ый фрагмент памяти')
        if архив_монстов.h2 == 3:
            архив_монстов.h2 += 1
            print('вы вспомнили 8-ый фрагмент памяти')
        if архив_монстов.h3 == 3:
            архив_монстов.h3 += 1
            print('вы вспомнили 9-ый фрагмент памяти')
        if архив_монстов.h4 == 3:
            архив_монстов.h4 += 1
            print('вы вспомнили 10-ый фрагмент памяти')
        if архив_монстов.d1 == 3:
            архив_монстов.d1 += 1
            print('вы вспомнили 11-ый фрагмент памяти')
        if архив_монстов.d2 == 3:
            архив_монстов.d2 += 1
            print('вы вспомнили 12-ый фрагмент памяти')
        if архив_монстов.d3 == 3:
            архив_монстов.d3 += 1
            print('вы вспомнили 13-ый фрагмент памяти')
        print(f'Вы выиграли!!!')
        main_game.tank()