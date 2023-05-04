import main_game
import hero
import invent
import lavochka
def k():
    print(f'''Ваши параметры уважаемый {hero.ran}: hp {hero.a}/{hero.a0+hero.a1+hero.a2+hero.a3}, dmg {hero.b}, def {hero.c}, 
ваш уровень {main_game.level}, количество опыта:{hero.l}/{hero.l0}, количество душ:{hero.con}''')
    print()
    a=input('''Вы находитесь в рюкзаке - вы можете выбрать:\nинвентарь - 'i'\nлавочка - 'l \nвыход отсюда - 'exit'
ввод: ''')
    print()
    if a=='l':
        lavochka.lavka()
    elif a=='i':
        invent.hay()
    elif a=='exit':
        main_game.tank()
    else:
        print('Вводите правильно данные!')
        return k()