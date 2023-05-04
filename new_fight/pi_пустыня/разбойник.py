from random import randint
a=100
b=12
c=9

name='разбойник'
def first_ability():
    print('критический удар-перезарядка три хода')
    print('воровской удар')
    return second_ability()+randint(b,b*2)
def second_ability():
    x=randint(3,b)
    z=randint(3,b)
    return x+z
def death(a,b):
    b+=20
    a+=13
    return a,b
