import hero
import галуши, футболка_месси, сандали, лахмотья, палка, ржавая_труба,сапог
import lavochka
import main_game
import invent

dmg=0
deff=0
hell=0
def buy():
    global dmg
    global deff
    global hell
    a=input(f'''Вы находитесь в магазине, {hero.con} - ваше количество душ\nВы можете купить:\nOружия - 'w'\nБроню - 'a'\nБотинки - 'b'\nСторонние предметы - 's'\nвыход в лавочку - 'lav'
выход к инвентарю - 'inv'\nвыход в меню - 'exit'\nВвод: ''')
    print()
    if a=='w':
        weapon = input(f'''Вы можете выбрать из оружия: 
палку - 'pal'
ржавую трубу - 'tru'
Ввод: ''')
        print()
        if weapon == 'pal':
            print(f'Ваши параметры будут увеличены:\n+{палка.a} hp\n+{палка.b} damage\n+{палка.c} defense')
            print('Способность: шанс нанести двойной удар\n')
            w = input('Вы хотите это купить? - Y or N')
            print()
            if w == 'Y':
                if hero.con>=20:
                    print(f'{hero.con}-20={hero.con-20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con-=20
                    палка.accept=0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        elif weapon == 'tru':
            print(f'Ваши параметры будут увеличены:\n+{ржавая_труба.a} hp\n+{ржавая_труба.b} damage\n+{ржавая_труба.c} defense')
            print("Способность: oтнимает 5хп но взамен дает +5 к урону\n")
            w = input('Вы хотите это купить? - Y or N ')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    ржавая_труба.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        else:
            print('Вводите правильно данные!')
            print()
            return buy()
    elif a=='a':
        armor=input(f'''Вы можете купить броню: 
лахмотья - 'lah'
футболку Месси  - 'fut'
Ввод: ''')
        print()
        if armor=='lah':
            print(f'Ваши параметры будут увеличены:\n+{лахмотья.a} hp \n+{лахмотья.b} damage \n+{лахмотья.c} defense')
            print("Способность: +2 ед к брони наносит\nгарантированно половину текущего урона\n")
            w = input('Вы хотите это купить? - Y or N ')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    лахмотья.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        elif armor=='fut':
            print(f'Ваши параметры будут увеличены:\n+{футболка_месси.a} hp\n+{футболка_месси.b} damage\n+{футболка_месси.c} defense')
            print(f"Способность: шанс нанести критический урон - от {hero.b} до {hero.b*2}\n")
            w = input('Вы хотите это купить? - Y or N ')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    футболка_месси.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        else:
            print('Вводите правильно данные!')
            print()
            return buy()
    elif a=='b':
        boots = input(f'''вы можете купить ботинки:
сандали - 'san'
галоши - 'gal'
сапог - 'sap'
Ввод: ''')
        print()
        if boots=='san':
            print(f'Ваши параметры будут увеличены:\n+{сандали.a} hp\n+{сандали.b} damage\n+{сандали.c} defence')
            print(f'Способность: удар от 0 до {hero.b*2}\n')
            w=input('Вы хотите это купить? - Y or N ')
            print()
            if w=='Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    сандали.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w=='N':
                return buy()
            else:
                print('вводите правильно данные!')
                print()
                return buy()
        elif boots=='gal':
            print(f'Ваши параметры будут увеличены:\n+{галуши.a} hp\n+{галуши.b} damage\n+{галуши.c} defense')
            print(f'Способность: при текущем уроне - урон от {hero.b//2} до {hero.b+hero.b//2}\nно -2 ед брони\n')
            w = input('Вы хотите это купить? - Y or N ')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    галуши.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        if boots=='sap':
            print(f'Ваши параметры будут увеличены:\n+{сапог.a} hp\n+{сапог.b} damage\n+{сапог.c} defence')
            print(f'Способность: во время битвы ставите себе щит в 10 едениц и востонавливаете 10 хп и также наносите 8 урона')
            w=input('Вы хотите это купить? - Y or N ')
            print()
            if w=='Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    сапог.accept = 0
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w=='N':
                return buy()
            else:
                print('вводите правильно данные!')
                print()
                return buy()
        else:
            print('Вводите правильно данные!')
            print()
            return buy()
    elif a=='s':
        a= input('''Вы можете купить баф:
баф хилка - 'h' 
баф демедж - 'd'
баф броня - 'a'
Ввод: ''')
        print()
        if a=='h':
            print("Баф хилка дает +20 хп")
            w = input('Вы хотите это купить? - Y or N ')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    hell += 1
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        elif a == 'd':
            print("Баф демедж удваивает урон")
            w = input('Вы хотите это купить? - Y or N')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    dmg += 1
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        elif a == 'a':
            print("Баф броня удваивает броню")
            w = input('Вы хотите это купить? - Y or N')
            print()
            if w == 'Y':
                if hero.con >= 20:
                    print(f'{hero.con}-20={hero.con - 20}')
                    print('Покупка совершена успешно')
                    print()
                    hero.con -= 20
                    deff += 1
                    return buy()
                else:
                    print('Вам не хватает душ')
                    print()
                    return buy()
            elif w == 'N':
                return buy()
            else:
                print('Вводите правильно данные!')
                print()
                return buy()
        else:
            print('Вводите правильно данные!')
            print()
            return buy()
    elif a == 'exit':
        main_game.tank()
    elif a=='inv':
        invent.hay()
    elif a=='lav':
        lavochka.lavka()
    else:
        print('Вводите правильно данные!')
        print()
        return buy()
