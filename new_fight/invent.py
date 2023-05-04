import menu_package
import hero
import галуши, футболка_месси, сандали, лахмотья, палка, ржавая_труба,кирка,серая_мантия,сапог,катана,пистолет,сапоги_ордена
import magazin

def hay():
    item = input('''Вы находитесь в инвентарe
вы можете выбрать:
оружие - 'w'\nброню - 'a'\nсапоги - 'b'\nвыход в рюкзак - 'exit'\nввойти магазин - 'mag' 
Ввод: ''')
    print()
    if item == 'w':
        weapon=input('''Вы здесь можете выбрать оружия: палка - 'pal', ржавая труба - 'tru', кирка - 'kir',катана - 'kat'
Ввод''')
        print()
        if weapon=='pal':
            if палка.accept == 0:
                hero.a -= hero.a1
                hero.b -= hero.b1
                hero.c -= hero.c1
                hero.a1, hero.b1, hero.c1 = палка.a, палка.b, палка.c
                hero.a += hero.a1
                hero.b += hero.b1
                hero.c += hero.c1
                hero.f1 = 2
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif weapon=='tru':
            if ржавая_труба.accept == 0:
                hero.a -= hero.a1
                hero.b -= hero.b1
                hero.c -= hero.c1
                hero.a1, hero.b1, hero.c1 = ржавая_труба.a, ржавая_труба.b, ржавая_труба.c
                hero.a += hero.a1
                hero.b += hero.b1
                hero.c += hero.c1
                hero.f1 = 1
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif weapon=='kir':
            if кирка.accept == 0:
                hero.a -= hero.a1
                hero.b -= hero.b1
                hero.c -= hero.c1
                hero.a1, hero.b1, hero.c1 = кирка.a, кирка.b, кирка.c
                hero.a += hero.a1
                hero.b += hero.b1
                hero.c += hero.c1
                hero.f1 = 3
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif weapon=='kat':
            if катана.accept == 0:
                hero.a -= hero.a1
                hero.b -= hero.b1
                hero.c -= hero.c1
                hero.a1, hero.b1, hero.c1 = катана.a,катана.b, катана.c
                hero.a += hero.a1
                hero.b += hero.b1
                hero.c += hero.c1
                hero.f1 = 4
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        else:
            print('Вводите правильно данные!\n')
            return hay()
    if item == 'a':
        armor=input('''Вы здесь можете выбрать броню: лахмотья 'lah' ,футболка Месси - 'fut',серая_мантия - 'ser',пистолет-наплечник - 'pis'
Ввод: ''')
        print()
        if armor=='lah':
            if лахмотья.accept==0:
                hero.a -= hero.a2
                hero.b -= hero.b2
                hero.c -= hero.c2
                hero.a2, hero.b2, hero.c2 = лахмотья.a, лахмотья.b, лахмотья.c
                hero.a += hero.a2
                hero.b += hero.b2
                hero.c += hero.c2
                hero.f2 = 2
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif armor=='fut':
            if футболка_месси.accept == 0:
                hero.a -= hero.a2
                hero.b -= hero.b2
                hero.c -= hero.c2
                hero.a2, hero.b2, hero.c2 = футболка_месси.a, футболка_месси.b, футболка_месси.c
                hero.a += hero.a2
                hero.b += hero.b2
                hero.c += hero.c2
                hero.f2 = 1
                print(f'Ваши параметры увеличены:hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif armor=='ser':
            if серая_мантия.accept == 0:
                hero.a -= hero.a2
                hero.b -= hero.b2
                hero.c -= hero.c2
                hero.a2, hero.b2, hero.c2 = серая_мантия.a, серая_мантия.b, серая_мантия.c
                hero.a += hero.a2
                hero.b += hero.b2
                hero.c += hero.c2
                hero.f2 = 3
                print(f'Ваши параметры увеличены:hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif armor=='pis':
            if пистолет.accept == 0:
                hero.a -= hero.a2
                hero.b -= hero.b2
                hero.c -= hero.c2
                hero.a2, hero.b2, hero.c2 = пистолет.a, пистолет.b, пистолет.c
                hero.a += hero.a2
                hero.b += hero.b2
                hero.c += hero.c2
                hero.f2 = 4
                print(f'Ваши параметры увеличены:hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        else:
            print('Вводите правильно данные!\n')
            return hay()
    elif item == 'b':
        boots=input('''Вы здесь можете выбрать ботинки: сандали - 'sal', галоши - 'gal',сапоги - 'sap',сапоги ордена - 'ord'
Ввод''')
        print()
        if boots=='san':
            if сандали.accept == 0:
                hero.a -= hero.a3
                hero.b -= hero.b3
                hero.c -= hero.c3
                hero.a3, hero.b3, hero.c3 = сандали.a, сандали.b, сандали.c
                hero.a += hero.a3
                hero.b += hero.b3
                hero.c += hero.c3
                hero.f3 = 2
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif boots=='gal':
            if галуши.accept == 0:
                hero.a -= hero.a3
                hero.b -= hero.b3
                hero.c -= hero.c3
                hero.a3, hero.b3, hero.c3 = галуши.a, галуши.b, галуши.c
                hero.a += hero.a3
                hero.b += hero.b3
                hero.c += hero.c3
                hero.f3 = 1
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif boots=='sap':
            if сапог.accept == 0:
                hero.a -= hero.a3
                hero.b -= hero.b3
                hero.c -= hero.c3
                hero.a3, hero.b3, hero.c3 = сапог.a, сапог.b, сапог.c
                hero.a += hero.a3
                hero.b += hero.b3
                hero.c += hero.c3
                hero.f3 = 3
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        elif boots=='ord':
            if сапоги_ордена.accept == 0:
                hero.a -= hero.a3
                hero.b -= hero.b3
                hero.c -= hero.c3
                hero.a3, hero.b3, hero.c3 = сапоги_ордена.a, сапоги_ордена.b, сапоги_ордена.c
                hero.a += hero.a3
                hero.b += hero.b3
                hero.c += hero.c3
                hero.f3 = 4
                print(f'Ваши параметры увеличены: hp {hero.a}, dmg {hero.b}, def {hero.c}')
                return hay()
            else:
                print('У вас этого предмета нету\n')
                return hay()
        else:
            print('Вводите правильно данные!\n')
            return hay()
    elif item == 'exit':
        menu_package.k()
    elif item == 'mag':
        magazin.buy()
    else:
        print('Вводите правильно данные!\n')
        return hay()