from random import randint

a=150
b=20
c=10
name='ядовитый_скорпион'
def first_ability():
    print('жало скорпиона')
    return b
def second_ability():
    x=randint(1,3)
    print('стрельба ядом')
    if x == 1:
        print('perfect shot')
        return randint(b,b*2)
    elif x == 2:
        print('попадение')
        return randint(0,b)
    elif x == 3:
        print('промах')
        return 0
def third_ability(den):
    print('doudle shield + attack')
    return den*2,randint(0,b)
def death(a,b):
    b+=30
    a+=15
    return a,b