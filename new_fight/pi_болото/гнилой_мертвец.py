from random import randint
a=140
b=12
c=2
name='гнилой_мертвец'
def first_ability(b):
    global a
    if b<=round(a*0.5):
        print(f'{b}+20={b+20}')
        print('перезарядка 3 хода после отхила')
        b=20+b
        return b
    else:
        return second_ability()
def second_ability():
    global b
    x=randint(3,b)
    return x
def death(a,b):
    b+=15
    a+=14
    return a,b