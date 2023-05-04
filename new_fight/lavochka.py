import hero
import menu_package
import magazin
def lavka():
    litem = input('''Вы находитесь в лавочкe;
Можете выбрать 
баф хилка - 'h'
демедж - 'd' 
броня - 'a'
магазин - 'mag'
выход отсюда - 'exit'

Ввод: ''')
    print()
    if litem=='mag':
        magazin.buy()
    elif litem == 'h':
        if magazin.hell>0:
            if hero.a+20 < hero.a1+hero.a2+hero.a3+hero.a0:
                magazin.hell-=1
                hero.a+=20
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return lavka()
            elif hero.a+20 > hero.a1+hero.a2+hero.a3+hero.a0:
                magazin.hell -= 1
                hero.a = hero.a1 + hero.a2 + hero.a3 + hero.a0
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return lavka()
            else:
                print('У вас уже максимальное здоровья')
                return lavka()
        else:
            print('К сожалению у вас нету этого предмета')
            return lavka()
    elif litem == 'd':
        if hero.i == 0:
            if magazin.dmg>0:
                hero.i = 1
                magazin.dmg-=1
                hero.b *= 2
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return lavka()
            else:
                print('К сожалению у вас нету этого предмета')
                return lavka()
        else:
            print('Вы уже выбрали данный баф')
            return lavka()
    elif litem == 'a':
        if magazin.deff>0:
            if hero.u == 0:
                magazin.deff-=1
                hero.u = 1
                hero.c *= 2
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return lavka()
            else:
                print('Вы уже выбрали данный баф')
                return lavka()
        else:
            print('К сожалению у вас нету этого предмета')
            return lavka()
    elif litem == 'exit':
        menu_package.k()
    else:
        print('вводите правильно данные!')
        return lavka()