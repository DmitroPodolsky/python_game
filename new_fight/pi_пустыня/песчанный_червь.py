from random import randint
a=160
b=0
c=20
name ='песчанный_червь'
def first_ability():
    print('dmg=def')
    global b
    global c
    if b==0:
        b=c
        c=0
        return randint(0,b)
    else:
        b+=2
        return second_ability()
def second_ability():
    print('def=dmg')
    global b
    global c
    global a
    if c == 0:
        c = b
        b = 0
        print(f'{a}+{c//4}={a+c//4}')
        a+=c//4
        return 0
    else:
        c += 2
        return first_ability()
def death(a,b):
    b+=25
    a+=16
    return a,b